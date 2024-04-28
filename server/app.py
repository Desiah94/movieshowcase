#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from flask import jsonify, request
from app import app, db
from models import User, Movie, Showtime, Review, Favorite

# Routes for Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'}), 200

# Routes for Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.to_dict())

@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.json
    new_movie = Movie(**data)
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    data = request.json
    for key, value in data.items():
        setattr(movie, key, value)
    db.session.commit()
    return jsonify(movie.to_dict())

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted'}), 200

# Routes for Showtimes
@app.route('/showtimes', methods=['GET'])
def get_showtimes():
    showtimes = Showtime.query.all()
    return jsonify([showtime.to_dict() for showtime in showtimes])

@app.route('/showtimes/<int:showtime_id>', methods=['GET'])
def get_showtime(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    return jsonify(showtime.to_dict())

@app.route('/showtimes', methods=['POST'])
def create_showtime():
    data = request.json
    new_showtime = Showtime(**data)
    db.session.add(new_showtime)
    db.session.commit()
    return jsonify(new_showtime.to_dict()), 201

@app.route('/showtimes/<int:showtime_id>', methods=['PUT'])
def update_showtime(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    data = request.json
    for key, value in data.items():
        setattr(showtime, key, value)
    db.session.commit()
    return jsonify(showtime.to_dict())

@app.route('/showtimes/<int:showtime_id>', methods=['DELETE'])
def delete_showtime(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    db.session.delete(showtime)
    db.session.commit()
    return jsonify({'message': 'Showtime deleted'}), 200

# Routes for Reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify(review.to_dict())

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    new_review = Review(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    data = request.json
    for key, value in data.items():
        setattr(review, key, value)
    db.session.commit()
    return jsonify(review.to_dict())

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted'}), 200

# Routes for Favorites
@app.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    return jsonify([favorite.to_dict() for favorite in favorites])

@app.route('/favorites/<int:favorite_id>', methods=['GET'])
def get_favorite(favorite_id):
    favorite = Favorite.query.get_or_404(favorite_id)
    return jsonify(favorite.to_dict())

@app.route('/favorites', methods=['POST'])
def create_favorite():
    data = request.json
    new_favorite = Favorite(**data)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.to_dict()), 201

@app.route('/favorites/<int:favorite_id>', methods=['PUT'])
def update_favorite(favorite_id):
    favorite = Favorite.query.get_or_404(favorite_id)
    data = request.json
    for key, value in data.items():
        setattr(favorite, key, value)
    db.session.commit()
    return jsonify(favorite.to_dict())

@app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    favorite = Favorite.query.get_or_404(favorite_id)
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

