#  "To-do tasks"  App
A simple task management application using Django, FastAPI, and Flask to demonstrate basic CRUD (Create, Read, Update, Delete) operations. The app features a clean and responsive UI styled with Bootstrap 5.
## Features
- List all tasks in a table format.
- Add new tasks using a form on a separate page.
- Edit and update existing tasks.
- Delete tasks with a confirmation alert.
- Styled with Bootstrap 5 for a responsive and clean UI.
## Requirements
**1.Django:**
 - Django
 - django-bootstrap-v5
   
**2.Fast API:**
 - FastAPI
 - Uvicorn
 - SQLAlchemy
 - Jinja2 (for HTML templating)

**3.Flask:** 
 - Flask
 - Flask-SQLAlchemy
 - Bootstrap 5 (via CDN)
## Installation & Setup
### Prerequisites
 Ensure you have **Python 3.x** installed on your system.
### Clone the repository
```
git clone https://github.com/Periyzat/API_Cruds.git
```
### Set up a virtual environment
```
python -m venv .venv
source .venv/bin/activate (On Windows use .venv\Scripts\activate)
```
### Install the dependencies
For Django:
`pip install django django-bootstrap-v5`
 
For Fast API: 
`pip install fastapi uvicorn sqlalchemy jinja2`

For Flask:
`pip install flask flask-sqlalchemy`
## Database Configuration
This project uses**SQLite** as the default database, which is lightweight and file-based, making it ideal for development and testing environments.
- **Django:** Automatically sets up an SQLite database `(db.sqlite3)` when you run migrations.
  `python manage.py migrate`
- **Fast API:** Creates an SQLite database file `(tasks.db)` when you run the application.
- **Flask:** Automatically generates an SQLite database `(db.sqlite3)` when you run the application.
 ## Running the Application
**Django:** 
`python manage.py runserver`
**Fast API:** 
`uvicorn main:app --reload`
**Flask:**
`flask run`
## Usage
- Open the browser and navigate to the corresponding localhost address.
- Use the interface to create, update, and delete tasks.
## Contributing
- Pull requests are welcome. For major changes, please open an issue first to discuss the proposed updates. 
## Licence
- This project is licensed under the MIT License.
