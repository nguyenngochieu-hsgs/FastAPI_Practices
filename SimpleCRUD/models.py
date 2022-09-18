from db import Base
from sqlalchemy import Column, String, TIMESTAMP, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Task(Base):
    __tablename__ = "Tasks"
    id = Column(String, primary_key = True, nullable=False)
    title = Column(String(1024), nullable=False)
    description = Column(String(2000), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)