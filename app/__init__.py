from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:c0mp2e5502@localhost:5432/postgres"

db = SQLAlchemy(app)

from app import routes
from app.models.book_model import Book
