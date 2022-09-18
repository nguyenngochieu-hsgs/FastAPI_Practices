import uvicorn
import uuid
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.params import Depends
from typing import List

import crud
from db import Base, engine, SessionLocal
from schemas import *

# Auto creation of database tables
#   If tables already exist, this command does nothing. This allows to 
#   safely execute this command at any restart of the application.
#   For a better management of the database schema, it is recommended to
#   integrate specific tools, such as Alembic
Base.metadata.create_all(bind=engine)

# This function represents a dependency that can be injected in the endpoints of the API.
# Dependency injection is very smart, as it allows to declaratively require some service.
# This function models the database connection as a service, so that it can be required
# just when needed.
def get_db():
    try:
        db = SessionLocal()
        yield db
    
    finally:
        db.close()

#Main app
app = FastAPI()

#api endpoints
@app.get("/tasks", response_model = List[TaskResponse])
async def get_all_tasks(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_tasks(db, limit)
 
@app.get("/tasks/{task_id}", response_model = TaskResponse)
async def get_task_by_id(task_id: str, db: Session = Depends(get_db)):
    return crud.get_task_by_id(db, task_id)

@app.post("/create_task", response_model = TaskResponse)
async def create_new_task(task: CreateTask, db: Session = Depends(get_db)):
    task_id = str(uuid.uuid4())
    return crud.create_task(db, task, task_id)

@app.put("/update_task/{task_id}", response_model = TaskResponse)
async def update_task(task_id: str, task: UpdateTask, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/delete_task/{task_id}", response_model = TaskResponse)
async def delete_task(task_id: str, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)

if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost", port=8001, reload=True)