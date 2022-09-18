from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = ""
    
class UpdateTask(BaseModel):
    title: Optional[str] = ""
    description: Optional[str] = ""
    
class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    
    class Config:
        orm_mode = True