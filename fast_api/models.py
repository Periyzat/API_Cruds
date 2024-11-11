from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
from datetime import date
from enum import Enum

# Enum for Priority Level (same as in SQLAlchemy model)
class PriorityLevel(str, Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

# SQLAlchemy Task Model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    description = Column(Text)
    due_date = Column(Date)
    priority = Column(String, default=PriorityLevel.MEDIUM)

# Pydantic BaseModel for Task (used for input validation)
class TaskBase(BaseModel):
    task: str
    description: str
    due_date: date
    priority: PriorityLevel = PriorityLevel.MEDIUM  # Default value

# TaskCreate schema (this is for creating a new task)
class TaskCreate(TaskBase):
    pass

# TaskRead schema (this is for reading a task)
class TaskRead(TaskBase):
    id: int

    class Config:
        orm_mode = True  # This is needed for FastAPI to convert ORM models to Pydantic models
