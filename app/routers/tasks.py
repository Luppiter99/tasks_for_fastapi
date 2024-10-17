from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from app.backend.db_depends import get_db
from app.models.task import Task
from app.schemas import CreateTask

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.get('/')
def get_all_tasks(db: Annotated[Session, Depends(get_db)],
                  skip: int = 0,
                  limit: int = 10):
    tasks = db.scalars(select(Task).offset(skip).limit(limit)).all()
    return tasks


@router.post('/create')
def create_task(task_data: CreateTask,
                db: Annotated[Session, Depends(get_db)]):
    db.execute(insert(Task).values(
        name=task_data.name,
        description=task_data.description,
        status=task_data.status))
    db.commit()
    return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }


@router.get('/{task_id}')
def get_task_detail(db: Annotated[Session, Depends(get_db)],
                    task_id: int
                    ):
    task = db.scalar(select(Task).where(Task.id == task_id))
    return task
