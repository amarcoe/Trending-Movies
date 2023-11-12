import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=False)

    def __repr__(self) -> str:
        return f"User with username: {self.username} created"

    def can_login(username, password):
        user = Users.query.filter_by(username=username).first()
        existing_user = user and check_password_hash(user.password, password)

        if existing_user:
            return existing_user
        else:
            return None

    def can_create(username):
        user = Users.query.filter_by(username=username).first()

        if user:
            return user
        else:
            return None

    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        user = Users(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


def create_table(app):
    with app.app_context():
        db.create_all()
