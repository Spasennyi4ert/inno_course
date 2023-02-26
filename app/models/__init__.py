from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db_objects(app):
    with app.app_context():
        global db
        db.create_all()


from .book_model import Book
