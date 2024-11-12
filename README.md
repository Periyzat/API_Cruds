#  "To-do tasks"  App
This is a simple application using Django, Fast API, and Flask to manage a list of "To-do tasks." It demonstrates basic CRUD (Create, Read, Update, Delete) operations with Bootstrap 5 styling.

## Features
- List all tasks in a table format.
- Add new tasks using a form on a separate page.
- Edit and update existing tasks.
- Delete tasks with a confirmation alert.
- Styled with Bootstrap 5 for a responsive and clean UI.
## Requirements

## Database
These project uses **SQLite** as the default database. SQLite is a lightweight, file-based database suitable for development and testing environments.
**Django** sets up automatically when you run migrations. By default, Django creates an SQLite database file named db.sqlite3 in the project directory.
**Fast API** sets up automatically when you run the application. By default, a file named tasks.db is created in your project directory to store data.
**Flask** sets up automatically when you run the application. By default, a file named db.sqlite3 is created in your project directory to store data.

## Installation
**1. Clone the repository:**
   **Django:** 
   **Fast API:** 
   **Flask:** 
**2. Set up a virtual environment and activate it:**
   python -m venv .venv
   source .venv/bin/activate (On Windows use .venv\Scripts\activate)
**3. Install the dependencies:**
    **Django:**
     pip install django django-bootstrap-v5
    **Fast API:** 
     pip install fastapi uvicorn sqlalchemy jinja2
    **Flask:** 
     pip install flask flask-sqlalchemy
**5. Set up the database:**
    **Django:**
     python manage.py makemigrations
     python manage.py migrate
    **Fast API:** 
    **Flask:** 
**6. Run the development server:
    **Django:** 
     python manage.py runserver
    **Fast API:** 
     uvicorn main:app --reload
    **Flask:**
     flask run
7. Access the app:**
   Open your browser and go to http://127.0.0.1:8000/.
## Usage
 - View Books: The homepage displays a list of all books in a table.
 - Add a Book: Click the "Add Book" button to go to a form page and add a new book.
 - Edit a Book: Click the "Edit" button next to a book to modify its details.
 - Delete a Book: Click the "Delete" button next to a book and confirm the deletion in the popup alert.
## Project Structure
- main.py: The main FastAPI application file that defines routes and initializes the app.
- database.py: Handles database setup and session creation using SQLAlchemy.
- models.py: Contains the Book model, which defines the structure of the database table in SQLite.
- schemas.py: Defines Pydantic schemas for data validation.
- templates/: Contains HTML templates.
- base.html: The base template with Bootstrap styling.
- book_list.html: Displays the list of books and an "Add Book" button.
- book_form.html: Used for adding and editing books.
- books.db: The SQLite database file where all data is stored (generated after running the app).
## Licence
