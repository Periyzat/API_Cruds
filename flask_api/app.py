from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an instance of SQLAlchemy
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.String(10), nullable=False)
    priority = db.Column(db.String(6), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for displaying the list of tasks
@app.route('/')
def task_list():
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

# Route for adding a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']

        # Create a new Task instance
        new_task = Task(task=task, description=description, due_date=due_date, priority=priority)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('task_list'))

    return render_template('task_form.html')

# Route for editing an existing task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.task = request.form['task']
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.priority = request.form['priority']

        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('task_list'))

    # Render the form with the current task details
    return render_template('task_form.html', task=task)

# Route for deleting a task
@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(debug=True)
