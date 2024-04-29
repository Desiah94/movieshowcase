#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify
from flask_restful import Resource, Api

# Local imports
from config import app, db
from models import User, Movie, Review, Showtime, Favorite

# Create the Flask-Restful API
api = Api(app)

# Flask-Restful Resources
class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.json
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

class UserDetailResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.json
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200

class MovieResource(Resource):
    def get(self):
        movies = Movie.query.all()
        return jsonify([movie.to_dict() for movie in movies])

    def post(self):
        data = request.json
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        return jsonify(new_movie.to_dict()), 201

class MovieDetailResource(Resource):
    def get(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        return jsonify(movie.to_dict())

    def put(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        data = request.json
        for key, value in data.items():
            setattr(movie, key, value)
        db.session.commit()
        return jsonify(movie.to_dict())

    def delete(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie deleted'}), 200

class ReviewResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return jsonify([review.to_dict() for review in reviews])

    def post(self):
        data = request.json
        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201

class ReviewDetailResource(Resource):
    def get(self, review_id):
        review = Review.query.get_or_404(review_id)
        return jsonify(review.to_dict())

    def put(self, review_id):
        review = Review.query.get_or_404(review_id)
        data = request.json
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.to_dict())

    def delete(self, review_id):
        review = Review.query.get_or_404(review_id)
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted'}), 200

class ShowtimeResource(Resource):
    def get(self):
        showtimes = Showtime.query.all()
        return jsonify([showtime.to_dict() for showtime in showtimes])

    def post(self):
        data = request.json
        new_showtime = Showtime(**data)
        db.session.add(new_showtime)
        db.session.commit()
        return jsonify(new_showtime.to_dict()), 201

class ShowtimeDetailResource(Resource):
    def get(self, showtime_id):
        showtime = Showtime.query.get_or_404(showtime_id)
        return jsonify(showtime.to_dict())

    def put(self, showtime_id):
        showtime = Showtime.query.get_or_404(showtime_id)
        data = request.json
        for key, value in data.items():
            setattr(showtime, key, value)
        db.session.commit()
        return jsonify(showtime.to_dict())

    def delete(self, showtime_id):
        showtime = Showtime.query.get_or_404(showtime_id)
        db.session.delete(showtime)
        db.session.commit()
        return jsonify({'message': 'Showtime deleted'}), 200

class FavoriteResource(Resource):
    def get(self):
        favorites = Favorite.query.all()
        return jsonify([favorite.to_dict() for favorite in favorites])

    def post(self):
        data = request.json
        new_favorite = Favorite(**data)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(new_favorite.to_dict()), 201

class FavoriteDetailResource(Resource):
    def get(self, favorite_id):
        favorite = Favorite.query.get_or_404(favorite_id)
        return jsonify(favorite.to_dict())

    def put(self, favorite_id):
        favorite = Favorite.query.get_or_404(favorite_id)
        data = request.json
        for key, value in data.items():
            setattr(favorite, key, value)
        db.session.commit()
        return jsonify(favorite.to_dict())

    def delete(self, favorite_id):
        favorite = Favorite.query.get_or_404(favorite_id)
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite deleted'}), 200

# Add resources to the API
api.add_resource(UserResource, '/users')
api.add_resource(UserDetailResource, '/users/<int:user_id>')
api.add_resource(MovieResource, '/movies')
api.add_resource(MovieDetailResource, '/movies/<int:movie_id>')
api.add_resource(ReviewResource, '/reviews')
api.add_resource(ReviewDetailResource, '/reviews/<int:review_id>')
api.add_resource(ShowtimeResource, '/showtimes')
api.add_resource(ShowtimeDetailResource, '/showtimes/<int:showtime_id>')
api.add_resource(FavoriteResource, '/favorites')
api.add_resource(FavoriteDetailResource, '/favorites/<int:favorite_id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
