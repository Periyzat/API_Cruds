from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Task

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create tables
Base.metadata.create_all(bind=engine)

# List Tasks
@app.get("/")
def read_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return templates.TemplateResponse("task_list.html", {"request": request, "tasks": tasks})

# Create Task
@app.get("/add", response_class=RedirectResponse)
def create_task_form(request: Request):
    return templates.TemplateResponse("task_form.html", {"request": request})

@app.post("/add")
def create_task(task: str = Form(...), description: str = Form(None), db: Session = Depends(get_db)):
    new_task = Task(task=task, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return RedirectResponse(url="/", status_code=303)

# Update Task
@app.get("/edit/{task_id}")
def edit_task(task_id: int, request: Request, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    return templates.TemplateResponse("task_form.html", {"request": request, "task": task})

@app.post("/edit/{task_id}")
def update_task(task_id: int, task: str = Form(...), description: str = Form(None), is_done: bool = Form(False), db: Session = Depends(get_db)):
    task_item = db.query(Task).filter(Task.id == task_id).first()
    task_item.task = task
    task_item.description = description
    task_item.is_done = is_done
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Delete Task
@app.post("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
