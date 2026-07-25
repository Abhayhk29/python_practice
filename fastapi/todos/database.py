from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALACHEMY_DATABASE_URL = "sqlite:///./todosa.db"
SQLALACHEMY_DATABASE_URL = "postgresql://postgres:abhay123@localhost/ToDoApplication"  # Update with your PostgreSQL connection string
engine = create_engine(SQLALACHEMY_DATABASE_URL)
# engine = create_engine(SQLALACHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

