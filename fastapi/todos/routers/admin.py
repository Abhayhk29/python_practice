from operator import gt
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Body, APIRouter, Depends, HTTPException, status, Path, Query
from ..models import Todo
from ..database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todos", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get("role") != "admin":
        raise HTTPException(status_code=401, detail="Authenticated as admin to access this resource")
    todos = db.query(Todo).all()
    return {"todos": todos}

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0, description="The ID of the todo to delete")):
    if user is None or user.get("role") != "admin":
        raise HTTPException(status_code=401, detail="Authenticated as admin to access this resource")
    
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.query(Todo).filter(Todo.id == todo_id).delete()
    # db.delete(todo)
    db.commit()