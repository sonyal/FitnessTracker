from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    search = StringField('Search for Workout Plan',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Search')
