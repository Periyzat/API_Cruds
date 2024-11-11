from flask_sqlalchemy import SQLAlchemy
from datetime import date
from enum import Enum

db = SQLAlchemy()

# Define Enum for Priority Choices
class PriorityLevel(Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

# Define your model here
class Task(db.Model):
    __tablename__ = 'list'  # Optional, to specify table name

    # Fields
    id = db.Column(db.Integer, primary_key=True)  
    task = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.Date, nullable=True)  # Allow due_date to be nullable if necessary
    priority = db.Column(db.Enum(PriorityLevel), default=PriorityLevel.MEDIUM, nullable=False)  # Use Enum for priority choices

    def __repr__(self):
        return f"<Task {self.task}>"
