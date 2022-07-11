from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    course = db.Column(db.Integer)
    group = db.Column(db.String(100))
    role = db.Column(db.String(20))
    faculty = db.Column(db.String(100))
    tasks = db.Column(db.Integer)