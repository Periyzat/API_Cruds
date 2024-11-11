from app import app, db  # Import the app and db from your main Flask application

with app.app_context():
    db.drop_all()  # This will drop all tables
    db.create_all()  # This will create tables based on the updated models
    print("Database tables recreated.")
