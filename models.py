from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plan(db.Model):
    # Model for plan which belongs to User
    # One User can have multi Plan
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.JSON)
    progress = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    # User Model which stores all the User information
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    weight = db.Column(db.String(30))
    height = db.Column(db.String(30))
    plans = db.relationship('Plan')
