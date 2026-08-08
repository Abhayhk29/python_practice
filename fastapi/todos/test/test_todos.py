from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..routers.todos import get_db, get_current_user
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from ..models import Todo

SQLALCHEMY_DATABASE_URL = "sqlite:///.testdb.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

def overide_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {"user_id": 1, "username": "testuser", 'role': "admin"}


app.dependency_overrides[get_db] = overide_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todo(title="Test Todo", description="This is a test todo", priority=1, complete=False, owner_id=1)
    
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute("DELETE FROM todos")
        connection.commit()


def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == 200
    # assert response.json() == {'todos': []}
    print(response.json())
    # assert response.json() == {'todos': [{'title': 'Test Todo', 'id': 1, 'description': 'This is a test todo', 'priority': 1, 'complete': False, 'owner_id': 1}]}
    assert response.status_code == status.HTTP_200_OK



def test_read_todo_authenticated_one(test_todo):
    response = client.get(f"/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"todo": {'title': 'Test Todo', 'id': 1, 'description': 'This is a test todo', 'priority': 1, 'complete': False, 'owner_id': 1}}


def test_read_todo_authenticated_not_found():
    response = client.get("/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_todo_authenticated():
    todo_data = {
        "title": "New Todo",
        "description": "This is a new todo",
        "priority": 2,
        "complete": False
    }
    response = client.post("/todos", json=todo_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.title == "New Todo").first()
    assert model.title == "New Todo"
    # assert response.json()["message"] == "Todo created successfully"
    # assert response.json()["todo"]["title"] == todo_data["title"]
    # assert response.json()["todo"]["description"] == todo_data["description"]
    # assert response.json()["todo"]["priority"] == todo_data["priority"]
    # assert response.json()["todo"]["complete"] == todo_data["complete"]



def test_update_todo_authenticated(test_todo):
    update_data = {
        "title": "Updated Todo",
        "description": "This is an updated todo",
        "priority": 3,
        "complete": True
    }
    response = client.put("/todos/1", json=update_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model.title == "Updated Todo"
    assert model.description == "This is an updated todo"
    assert model.priority == 3
    assert model.complete is True


def test_delete_todo_authenticated(test_todo):
    response = client.delete("/todos/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # db = TestingSessionLocal()
    # model = db.query(Todo).filter(Todo.id == 1).first()
    # assert model is None