from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer,)
    book_name = db.Column(db.String(100),)
    book_genre = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    book_description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class User(db.Model , UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
