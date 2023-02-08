from app import app, db
from datetime import datetime


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    description = db.Column(db.Text)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f'<Book {self.title}>'
