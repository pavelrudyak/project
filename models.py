from flask_login import UserMixin
from datetime import datetime
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

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_from = db.Column(db.Integer)
    user_to = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    '''def __init__(self, title, id, text, user_to):
        self.id = id
        self.title = title
        self.text = text
        self.user_to = user_to

    def __repr__(self):
        return '<Tasks %r' % self.id
'''

class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)
    file = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<Files %r' % self.id