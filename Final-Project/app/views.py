from flask import Blueprint, render_template, redirect, url_for, flash
from . import db
from .models import User, Movie, Review
from .forms import ReviewForm, RegisterForm, LoginForm

from flask_login import login_user, login_required, logout_user, current_user
from .utilities.movies import movies_list

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.movie_list'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/movies')
@login_required
def movie_list():
    movies = movies_list
    return render_template('movie_list.html', movies=movies)

@main.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(content=form.content.data, rating=form.rating.data,
                        user_id=current_user.id, movie_id=movie_id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been posted!', 'success')
        return redirect(url_for('main.movie_detail', movie_id=movie_id))
    return render_template('movie_detail.html', movie=movie, form=form)