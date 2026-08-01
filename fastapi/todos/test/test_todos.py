from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..routers.todos import get_db, get_current_user
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status

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

def test_read_all_authenticated():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK




