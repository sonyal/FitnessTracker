from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')


class WorkOutForm(FlaskForm):
    weight = StringField('Enter Your Weight')
    height = StringField('Enter Your height')
    submit = SubmitField('Submit')