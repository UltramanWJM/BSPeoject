from initDatabase import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Integer


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    phone = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

class Scenes(db.Model):
    __tablename__ = "Scenes"
    sceneId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    sceneName = db.Column(db.String(30), nullable=False, unique=True)
    userId = db.Column(db.Integer, nullable=False)
    imgPath = db.Column(db.String(128), nullable=False)
    deviceNumber = db.Column(db.Integer, nullable=False)

class Devices(db.Model):
    __tablename__ = "Devices"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    deviceName = db.Column(db.String(30), nullable=False, unique=True)
    sceneId = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    deviceType = db.Column(db.Integer, nullable=False)
    positionX = db.Column(db.Float, nullable=False)
    positionY = db.Column(db.Float, nullable=False)
