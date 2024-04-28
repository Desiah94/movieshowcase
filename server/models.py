from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

# Association table for many-to-many relationship between Users and Movies (Favorites)
favorite = db.Table(
    'favorite',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
)

class User(db.Model, SerializerMixin):
    serialize_rules = ('-password_hash',)
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)
    favorite_movies = db.relationship('Movie', secondary='favorite', backref='users')

class Movie(db.Model, SerializerMixin):
    serialize_rules = ('-reviews.movie',)
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)  # Duration in minutes
    reviews = db.relationship('Review', backref='movie', lazy=True)

class Review(db.Model, SerializerMixin):
    serialize_rules = ('-user.reviews', '-movie.reviews',)
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
