from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#use sqlite
DB_URL = "sqlite:///./database.db"

#create new engine instance
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

#create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()