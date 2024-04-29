# Import necessary libraries
from config import app, db
from models import User, Movie, Review, Favorite, Showtime
from faker import Faker
from random import randint, sample
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

def seed_data():
    # Clear existing data
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Generate users
        users = []
        for _ in range(10):
            user = User(
                username=fake.user_name(),
                name=fake.name(),
                email=fake.email(),
                password_hash=fake.password()
            )
            users.append(user)

        db.session.add_all(users)
        db.session.commit()

        # Generate movies
        movies = []
        for _ in range(10):
            movie = Movie(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                release_date=fake.date_between(start_date='-1y', end_date='today'),
                duration=randint(60, 180)
            )
            movies.append(movie)

        db.session.add_all(movies)
        db.session.commit()

        # Generate reviews
        for movie in movies:
            for _ in range(randint(1, 5)):
                review = Review(
                    rating=randint(1, 5),
                    review_text=fake.paragraph(),
                    timestamp=fake.date_time_this_year(),
                    user_id=randint(1, len(users)),
                    movie_id=movie.id
                )
                db.session.add(review)

        db.session.commit()

        # Generate favorites
        for user in users:
            favorite_movies = sample(movies, randint(1, 3))
            for movie in favorite_movies:
                favorite = Favorite(
                    user_id=user.id,
                    movie_id=movie.id
                )
                db.session.add(favorite)

        db.session.commit()

        # Generate showtimes
        for movie in movies:
            for _ in range(3):
                showtime = Showtime(
                    movie_id=movie.id,
                    time=datetime.now() + timedelta(days=randint(1, 30))
                )
                db.session.add(showtime)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
