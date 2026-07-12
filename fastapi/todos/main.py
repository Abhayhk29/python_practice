from operator import gt
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Body, FastAPI, Depends, HTTPException, status, Path, Query
import models
from models import Todo
from database import SessionLocal, engine
from routers import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=200)
    priority: int = Field(gt=0, le=5)
    complete: bool = False


@app.get("/todos", status_code=status.HTTP_200_OK)
async def read_todos(db: db_dependency):
    todos = db.query(Todo).all()
    return {"todos": todos}


@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency,todo_id: int = Path(gt=0, description="The ID of the todo to retrieve")):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"todo": todo}


@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    new_todo = Todo(**todo_request.model_dump())
    db.add(new_todo)
    db.commit()
    # db.refresh(new_todo)
    return {"message": "Todo created successfully", "todo": new_todo}


@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
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


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0, description="The ID of the todo to delete")):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    # return {"message": "Todo deleted successfully"}




