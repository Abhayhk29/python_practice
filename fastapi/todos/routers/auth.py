from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt

# router = APIRouter(
#     prefix="/auth",
#     tags=["auth"],
#     responses={404: {"message": "Not found"}}
# )

router = APIRouter()


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)    

SECRET_KEY = "random_secret_key" 
ALGORITHM = "HS256"  # Algorithm used for encoding the JWT

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    print(f"Authenticating user: {username}, Found user: {user}")
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username:str,user_id:int, role:str, expires_delta: timedelta):
    to_encode = {"sub": username, "user_id": user_id, "role": role}
    to_encode["exp"] = datetime.now(timezone.utc) + expires_delta
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class createUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=100)
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=6, max_length=100)
    role: str = Field(default="user", max_length=20)  # Default role is 'user'

class Token(BaseModel):
    access_token: str
    token_type: str

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        role: str = payload.get("role")
        if username is None or user_id is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return {"username": username, "user_id": user_id, "role": role}
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: createUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),  # In a real application, you should hash the password
        role=create_user_request.role,
        is_active=True
    )
    db.add(create_user_model)
    db.commit()
    # db.refresh(create_user_model) // what is the purpose of this line? It refreshes the instance with the latest data from the database, including any default values or auto-generated fields. You might want to uncomment it if you need to access those updated fields after committing.
    return {"message": "User created successfully", "user": create_user_model}
    # Here you would typically add the user to the database

@router.get('/getUsers', status_code=status.HTTP_200_OK)
async def read_users(db: db_dependency):
    users = db.query(Users).all()
    return {"users": users}

# @router.post('/token', status_code=status.HTTP_200_OK)
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         return {"message": "Invalid credentials"}
#     # Here you would typically generate a token
#     return {"message": "Token generated successfully"}


@router.post("/token",response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")
    # Here you would typically generate a token
    access_token = create_access_token(
        username=user.username,
        user_id=user.id,
        role=user.role,
        expires_delta=timedelta(minutes=30)  # Token expires in 30 minutes
    )
    return {"access_token": access_token, "token_type": "bearer"}


# JWT token generation and validation would typically be implemented here, but for simplicity, this example just returns a success message. In a real application, you would use a library like PyJWT to generate and validate JWT tokens.
# Is created of three seperate parts seperated by dots
# Header.Payload.Signature


