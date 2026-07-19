# from fastapi import APIRouter

# # router = APIRouter(
# #     prefix="/auth",
# #     tags=["auth"],
# #     responses={404: {"message": "Not found"}}
# # )

# router = APIRouter()

from operator import gt
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Body, APIRouter, Depends, HTTPException, status, Path, Query
from models import Todo
from database import SessionLocal
from .auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=200)
    priority: int = Field(gt=0, le=5)
    complete: bool = False
    # owner_id: int = Field(gt=0, description="The ID of the user who owns the todo")


@router.get("/todos", status_code=status.HTTP_200_OK)
async def read_todos(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    todos = db.query(Todo).filter(Todo.owner_id == user["user_id"]).all()
    return {"todos": todos}


@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0, description="The ID of the todo to retrieve")):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user["user_id"]).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"todo": todo}


@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    print(f"Creating todo for user: {user['username']} (ID: {type(user['user_id'])})")
    # return {"message": "Todo created successfully", "todo": todo_request}
    new_todo = Todo(**todo_request.model_dump(), owner_id=user["user_id"])
    db.add(new_todo)
    db.commit()
    # db.refresh(new_todo)
    return {"message": "Todo created successfully", "todo": new_todo}


@router.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_id: int = Path(gt=0, description="The ID of the todo to update"), todo_request: TodoRequest = Body(...)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete
    db.add(todo)
    db.commit()
    # for key, value in todo_request.model_dump().items():
    #     setattr(todo, key, value)
    # db.commit()
    # return {"message": "Todo updated successfully", "todo": todo}


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0, description="The ID of the todo to delete")):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    # return {"message": "Todo deleted successfully"}




