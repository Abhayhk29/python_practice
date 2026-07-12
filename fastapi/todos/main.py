from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Body, FastAPI, Depends
import models
from models import Todo
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/todos")
async def read_todos(db: db_dependency):
    todos = db.query(Todo).all()
    return {"todos": todos}