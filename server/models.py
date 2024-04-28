from config import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    serialize_rules = ('-password_hash',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Movie(db.Model, SerializerMixin):
    serialize_rules = ('-reviews.movie', '-showtimes.movie', '-favorites.movie')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)  # Duration in minutes
    reviews = db.relationship('Review', backref='movie', lazy=True)
    showtimes = db.relationship('Showtime', backref='movie', lazy=True)
    favorites = db.relationship('Favorite', backref='movie', lazy=True)

class Review(db.Model, SerializerMixin):
    serialize_rules = ('-user.reviews', '-movie.reviews', '-showtime.reviews')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'))

class Favorite(db.Model, SerializerMixin):
    serialize_rules = ('-user.favorites', '-movie.favorites')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

class Showtime(db.Model, SerializerMixin):
    serialize_rules = ('-movie.showtimes', '-reviews.showtime')

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
