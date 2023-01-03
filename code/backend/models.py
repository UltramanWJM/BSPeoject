from initDatabase import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Integer, text


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

class Lights(db.Model):
    __tablename__ = "Lights"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    luminance = db.Column(db.Integer, nullable=False)

class Switches(db.Model):
    __tablename__ = "Switches"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class Sensors(db.Model):
    __tablename__ = "Sensors"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class Lockes(db.Model):
    __tablename__ = "Lockes"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class DeviceMes(db.Model):
    __tablename__ = "DeviceMes"
    deviceId = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    info = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=text('CURRENT_TIMESTAMP'))
    valid = db.Column(db.Integer, nullable=False)