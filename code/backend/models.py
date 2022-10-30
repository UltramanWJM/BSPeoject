from initDatabase import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Integer


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    phone = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
