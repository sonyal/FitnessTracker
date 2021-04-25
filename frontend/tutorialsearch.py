from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class TestLinkProxy:
    def __init__(self):
        self.deck = {}

    def test_link(self, link):
        if not isinstance(link, str):
            return -1
        if link == "Cardiovascular" or link == "cardiovascular":
            return 0
        if link == "Flexibility" or link == "flexibility":
            return 1
        if link == "Strength" or link == "strength":
            return 2
        return -1


class RegistrationForm(FlaskForm):
    search = StringField('Search for Workout Plan', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Search')
