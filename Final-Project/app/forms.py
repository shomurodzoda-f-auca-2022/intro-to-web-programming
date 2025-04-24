from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
    content = TextAreaField('Review', validators=[DataRequired(), Length(min=10)])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField('Submit')