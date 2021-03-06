from flask_login import UserMixin

from lowelldevclub import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class ShortLink(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    link = db.Column(db.String(200), unique=True, nullable=False)
    timesused = db.Column(db.Integer, unique=False, nullable=False)


class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    repoUrl = db.Column(db.String(100), unique=False, nullable=True)
    workshopMD = db.Column(db.String(150), unique=False, nullable=True)
    text = db.Column(db.String(1500), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, unique=False)
    timesviewed = db.Column(db.Integer, nullable=False, unique=False)
