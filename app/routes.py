from app import app, db
from flask import render_template, request
from app.models.book_model import Book


@app.route("/")
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route("/book", methods=['POST', 'GET'])
def book():
    if request.method == 'POST':
        b = Book(title=request.form['title'],
                 author=request.form['author'],
                 genre=request.form['genre'],
                 rating=request.form['rating'],
                 description=request.form['description'],
                 notes=request.form['notes']
        )
        db.session.add(b)
        db.session.commit()
    return render_template('book.html', title='Book')
