import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.Integer, nullable=True)
    comments = db.Column(db.String(500), nullable=True)
    ratings = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return f"User with username: {self.username} created"

    def authenticate(username):
        user = Users.query.filter_by(username=username).first()
        if user:
            return user
        else:
            return None


def create_table(app):
    with app.app_context():
        db.create_all()
