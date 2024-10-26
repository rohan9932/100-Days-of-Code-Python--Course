# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# # creating a database
# cursor.execute(
#     "CREATE TABLE books ("
#     "id INTEGER PRIMARY KEY, "
#     "title varchar(250) NOT NULL UNIQUE, "
#     "author varchar(250) NOT NULL, "
#     "rating FLOAT NOT NULL"
#     ")"
# )

# # adding in a data base
# cursor.execute(
#     "INSERT INTO books VALUES ("
#     "1,"
#     "'The Psychology of Money',"
#     "'Morgan Housel',"
#     "8.6"
#     ")"
# )
# db.commit()


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# Initializing
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Initializing the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# creating the tables
with app.app_context():
    db.create_all()

# # creating a new record
# with app.app_context():
#     new_book = Book(id=4, title="Hello", author="J.K. Rowling", rating=9.5)
#     db.session.add(new_book)
#     db.session.commit()
#
# # read all records
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars().all()
#
#     print(list(all_books))
#
# # read a particular book
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     print(book)

# # update by query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Philosopher's Stone"
#     db.session.commit()

# # update by primary key
# book_id = 1
# with app.app_context():
#     book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.rating = 9
#     db.session.commit()

# # delete a record
# delete_book_record = 4
# with app.app_context():
#     book_to_delete = db.get_or_404(Book, delete_book_record)
#     db.session.delete(book_to_delete)
#     db.session.commit()
#
