import json
from faker import Faker
from app import db
from models import User, Movie, Review, ShowTime, Favorite
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from random import choice
from datetime import datetime, timedelta, time

# Instantiate Faker object
fake = Faker()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.strftime('%H:%M')
        return json.JSONEncoder.default(self, obj)

def calculate_hours(clock_in, clock_out):
    """Calculate hours between two time objects."""
    start = datetime.combine(datetime.min, clock_in)  # Combine with minimum date
    end = datetime.combine(datetime.min, clock_out)  # Combine with minimum date
    duration = end - start
    total_hours = duration.total_seconds() / 3600  # Convert seconds to hours
    if total_hours < 0:
        total_hours += 24  # Adjust for overnight work
    return round(total_hours, 2)  # Round to two decimal places

def seed_database():
    # Clear existing data
    db.session.query(Review).delete()
    db.session.query(ShowTime).delete()
    db.session.query(Favorite).delete()
    db.session.query(User).delete()
    db.session.query(Movie).delete()
    db.session.commit()

    # Seed users
    users = []
    for _ in range(10):
        user_data = {
            'username': fake.user_name(),
            'email': fake.email(),
            'password_hash': generate_password_hash(fake.password())
        }
        users.append(User(**user_data))
    db.session.bulk_save_objects(users)
    db.session.commit()

    # Fetch users from the database
    users = User.query.all()

    # Seed movies
    movies = []
    for _ in range(10):
        movie_data = {
            'title': fake.catch_phrase(),
            'description': fake.paragraph(),
            'release_date': fake.date(),
            'duration': fake.random_int(min=60, max=180)  # Duration in minutes
        }
        movies.append(Movie(**movie_data))
    db.session.bulk_save_objects(movies)
    db.session.commit()

    # Fetch movies from the database
    movies = Movie.query.all()

    # Seed reviews
    for movie in movies:
        for _ in range(3):  # Assume 3 reviews per movie
            review_data = {
                'rating': fake.random_int(min=1, max=5),
                'review_text': fake.paragraph(),
                'timestamp': fake.date_time_this_year(),
                'user_id': choice(users).id,
                'movie_id': movie.id
            }
            review = Review(**review_data)
            db.session.add(review)
    db.session.commit()

    # Seed show times
    for movie in movies:
        for _ in range(3):  # Assume 3 show times per movie
            start_time = fake.time_object(end_datetime=None)
            end_time = start_time + timedelta(hours=fake.random_int(min=1, max=3))
            duration = calculate_hours(start_time, end_time.time())
            show_time_data = {
                'movie_id': movie.id,
                'start_time': start_time.time(),
                'end_time': end_time.time(),
                'duration': duration
            }
            show_time = ShowTime(**show_time_data)
            db.session.add(show_time)
    db.session.commit()

    # Seed favorites
    for _ in range(20):  # Assume 20 favorites in total
        favorite_data = {
            'user_id': choice(users).id,
            'movie_id': choice(movies).id
        }
        favorite = Favorite(**favorite_data)
        db.session.add(favorite)
    db.session.commit()

    print("Database seeded successfully.")

    # Serialize datetime objects to JSON
    with open('seed_data.json', 'w') as json_file:
        seed_data = {
            'users': [user.to_dict() for user in users],
            'movies': [movie.to_dict() for movie in movies],
            'reviews': [review.to_dict() for review in Review.query.all()],
            'show_times': [show_time.to_dict() for show_time in ShowTime.query.all()],
            'favorites': [favorite.to_dict() for favorite in Favorite.query.all()]
        }
        json.dump(seed_data, json_file, cls=DateTimeEncoder)

if __name__ == '__main__':
    seed_database()
