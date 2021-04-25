from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Log in')

class SignUpForm(FlaskForm):
    username = StringField('Enter Your Username')
    password = PasswordField('Enter Your Password')
    confirm_password = PasswordField('Comfirm Your Password')
    weight = StringField('Enter Your Weight')
    height = StringField('Enter Your Height')
    submit = SubmitField('Sign up')