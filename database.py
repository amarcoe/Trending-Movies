import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.Integer, nullable=True)
    comments = db.Column(db.String(500), nullable=True)
    ratings = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return f"Person with username: {self.username} created"

    # TODO: Create an authenticator function


def create_table(app):
    with app.app_context():
        db.create_all()
