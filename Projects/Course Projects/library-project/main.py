from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# create database
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[str] = mapped_column(String, nullable=False)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db.init_app(app)

# create table schema in the database
with app.app_context():
    db.create_all()



@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = results.scalars().all()
    return render_template('index.html', books=list(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_details = {
            'title': request.form['name'],
            'author': request.form['author'],
            'rating': request.form['rating']
        }
        new_book = Book(title=book_details['title'], author=book_details['author'], rating=book_details['rating'])
        db.session.add(new_book)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        # update rating
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect('/')
    
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit_rating.html', book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

