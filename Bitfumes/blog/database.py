from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DataBase Connection Using sqlalchemyORM
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' # Connection to SQLite

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Each request gets its own database connection session

Base = declarative_base() #We will inherit from this class to create each of the database models or classes (the ORM models)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()