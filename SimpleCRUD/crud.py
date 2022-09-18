from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas import *
from models import Task
from fastapi import HTTPException

def get_all_tasks(db: Session, limit: int):
    try:
        all_tasks = db.query(Task).limit(limit).all()
        return all_tasks
    
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

def get_task_by_id(db: Session, task_id: str):
    try:
        existedTask = db.query(Task).get(task_id)
        return TaskResponse.from_orm(existedTask)
    
    except Exception:
        raise HTTPException(status_code=404, detail="Task with id {task_id} not found".format(task_id=task_id))

def create_task(db: Session, task: CreateTask, task_id: str):
    try:
        existedTask = db.query(Task).get(task_id)
        if existedTask:
            raise HTTPException(status_code=409, detail="Task with id {task_id} has been existed, please create new task again".format(task_id=task_id))
        
        else:
            task_obj = Task(
                id = task_id,
                title = task.title,
                description = task.description
            )
            db.add(task_obj)
            db.commit()
            db.refresh(task_obj)
            return task_obj
    
    except SQLAlchemyError as e:
        print(e)
        
def update_task(db: Session, task_id: str, new_task: UpdateTask):
    try:
        existedTask = db.query(Task).get(task_id)
        if not existedTask:
            raise HTTPException(status_code=404, detail="Task with id {task_id} not found".format(task_id=task_id))
        
        else:
            if new_task.title:
                existedTask.title = new_task.title
            
            if new_task.description:
                existedTask.description = new_task.description
            db.commit()
            db.refresh(existedTask)
            return existedTask
    
    except SQLAlchemyError as e:
        print(e)
        
def delete_task(db: Session, task_id: str):
    try:
        existedTask = db.query(Task).get(task_id)
        if not existedTask:
            raise HTTPException(status_code=404, detail="Task with id {task_id} not found".format(task_id=task_id))
        
        else:
            db.delete(existedTask)
            db.commit()
            return existedTask
        
    except SQLAlchemyError as e:
        print(e)