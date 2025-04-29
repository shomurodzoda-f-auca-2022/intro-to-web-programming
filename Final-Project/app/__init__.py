from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .views import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

def seed_movies():
    from .models import Movie
    from .utilities.movies import movies_list

    for movie in movies_list:
        existing = Movie.query.filter_by(title=movie['title']).first()
        if not existing:
            new_movie = Movie(
                title=movie['title'],
                description=movie['description'],
                year=movie['year']
            )
            db.session.add(new_movie)
    db.session.commit()
    print("Movies seeded.")