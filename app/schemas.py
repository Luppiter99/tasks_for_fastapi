from pydantic import BaseModel
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    new = 'новая'
    in_progress = 'в процессе'
    completed = 'завершена'


class CreateTask(BaseModel):
    name: str
    description: str
    status: TaskStatus


class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
