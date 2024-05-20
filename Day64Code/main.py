from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, func
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app, model_class=Base)

class Movie(db.Model):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking).all()

    for movie in all_movies:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute('SELECT img_url FROM movies WHERE id = ?', (movie.id,))
        result = cursor.fetchone()
        if result is not None:
            movie.img_url = result[0]
        cursor.close()
        conn.close()
    if not all_movies:
        return "No movies found in the database.", 404
    return render_template("index.html", movies=all_movies)


@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("delete_movie.html", movie=movie)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT img_url FROM movies WHERE id = ?', (movie.id,))
    movie.img_url = cursor.fetchone()[0]
    if request.method == "POST":
        movie.rating = request.form["rating"]
        movie.ranking = request.form["ranking"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        description = request.form["description"]
        rating = request.form["rating"]
        review = request.form["review"]
        img_url = request.form["img_url"]
        ranking = request.form["ranking"]
        new_movie = Movie(title=title, year=year, description=description, rating=rating, ranking=ranking, review=review, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
