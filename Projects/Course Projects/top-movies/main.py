from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

TMDB_API_KEY = os.environ["TMDB_API_KEY"]

# FUNCTIONS
def find_movie(movie_title):
    tmdb_api_key = TMDB_API_KEY
    parameters = {
        "api_key": tmdb_api_key,
        "query": movie_title
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie" , params=parameters)
    movie_options = response.json()["results"]

    return movie_options


# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# FORM
class UpdateForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 8', validators=[DataRequired()])
    review = StringField('Your Review')
    submit = SubmitField('Done')

class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    results = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = results.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=list(all_movies))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    update_form = UpdateForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)

    if update_form.validate_on_submit():
        if len(update_form.review.data) == 0:
            movie.rating = float(update_form.rating.data)
            db.session.commit()
        else:
            movie.rating = float(update_form.rating.data)
            movie.review = update_form.review.data
            db.session.commit()

        return redirect(url_for('home'))
    
    return render_template("edit.html", form=update_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    delete_movie = db.get_or_404(Movie, movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_movie = AddMovie()
    if add_movie.validate_on_submit():
        movie_name = add_movie.title.data
        data = find_movie(movie_name)

        return render_template("select.html", movie_options=data)
        
    return render_template("add.html", add_form=add_movie)


@app.route("/find")
def movie_finder():
    movie_id = request.args.get('id')
    if movie_id:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params={"api_key": TMDB_API_KEY})
        data = response.json()
        new_movie = Movie(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            description = data["overview"],
            img_url = f"https://image.tmdb.org/t/p/original/{data['poster_path']}",
            rating = 0,
            review = "write some",
            ranking = data["popularity"]

        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
