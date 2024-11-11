from flask_sqlalchemy import SQLAlchemy
from datetime import date
from enum import Enum

db = SQLAlchemy()
from pydantic import BaseModel

class TaskBase(BaseModel):
    task: str
    description: str
    due_date: int
    priority: str = None

class BookCreate(TaskBase):
    pass

class Book(TaskBase):
    id: int

    class Config:
        orm_mode = True
