from sqlalchemy import create_engine
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
    assert response.json() == {'todos': [{'title': 'Test Todo', 'description': 'This is a test todo', 'priority': 1, 'complete': False, 'owner_id': 1}]}
    # assert response.status_code == status.HTTP_200_OK




