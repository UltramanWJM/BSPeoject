import json

from flask import Flask, jsonify, request, flash
from flask_cors import CORS
from initDatabase import createApp
from initDatabase import db
from models import Users, Scenes
from flask_sqlalchemy import SQLAlchemy

app = createApp()
CORS(app)

def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data

@app.route('/', methods=['GET'])
def first():
    return jsonify('Test1')

@app.route('/test', methods=['GET'])
def second():
    return jsonify('Test2')

@app.route('/login', methods=['GET'])
def login():
    data = request_parse(request)
    id = data.get('id')
    pwd = data.get('password')
    user = Users.query.filter(Users.id == id, Users.password == pwd).first()
    print(user)
    print(user.phone)
    if user:
        msg = "登陆成功"
        code = 1
        name = user.username
        phone = user.phone
    else:
        msg = "登录失败"
        code = 0
    return jsonify(code = code, msg = msg, name = name, phone = phone)


@app.route('/register', methods=['POST', 'GET'])
def register():
    data = request_parse(request)
    username = data.get('username')
    id = data.get('id')
    phone = data.get('phone')
    password = data.get('password')
    print(id, username, phone, password)
    res = {
        "code": 1,
        "msg": "Register Success!"
    }
    users = Users.query.all()
    for user in users:
        if id == user.id or phone == user.phone:
            res['code'] = 0
            res['msg'] = "ID or Phone existed!"
            return res
    newUser = Users(id=id, username=username, phone=phone, password=password)
    db.session.add(newUser)
    db.session.commit()
    return res


@app.route('/modusr', methods=['GET'])
def modusr():
    data = request_parse(request)
    id = data.get('id')
    type = int(data.get('type'))
    user = Users.query.filter(Users.id == id).first()
    res = {
        "code": 1,
        "msg": "Modify Success!"
    }
    if type == 0: # modify name
        user.username = data.get('name')
        # print(user.username)
    elif type == 1: # modify phone
        phone = data.get('phone')
        isExist = Users.query.filter(Users.phone == phone).first()
        if isExist:
            res['code'] = 0
            res['msg'] = "Already exist the phone number!"
            return res
        user.phone = data.get('phone')
    elif type == 2: # modify password
        user.password = data.get('password')
    db.session.commit()
    return res


@app.route('/getuserinfo', methods=['GET'])
def getUserinfo():
    data = request_parse(request)
    id = data.get('id')
    print(id)
    user = Users.query.filter(Users.id == id).first()
    res = {
        "id": id,
        "name": user.username,
        "phone": user.phone,
        "password": user.password
    }
    return res

@app.route('/storeimg', methods=['GET', 'POST'])
def storeImg():
    img = request.files.get('file')
    path = "./imgs/"
    imgName = img.filename
    filePath = path + imgName
    img.save(filePath)
    return filePath

@app.route('/createscene', methods=['GET', 'POST'])
def createScene():
    data = request_parse(request)
    sceneId = data.get('newSceneId')
    sceneName = data.get('newSceneName')
    userId = data.get('userId')
    imgPath = data.get('image')
    scenes = Scenes.query.filter(Scenes.sceneId == sceneId).first()
    res = {
        "code": 1,
        "msg": ""
    }
    if (scenes):
        res["code"] = 0
        res["msg"] = "Already exist scenesID " + sceneId
        return res
    newScene = Scenes(sceneId=sceneId, sceneName=sceneName, userId=userId, imgPath=imgPath, deviceNumber=0)
    db.session.add(newScene)
    db.session.commit()
    res["msg"] = "新场景创建成功"
    return res

@app.route('/getscenes', methods=['GET', 'POST'])
def getScenes():
    data = request_parse(request)
    userId = data.get('userId')
    scenes = Scenes.query.filter(Scenes.userId == userId).all()
    ret = {
        "code": 1,
        "data": []
    }
    for scene in scenes:
        sce = {
            "sceneId": scene.sceneId,
            "sceneName": scene.sceneName,
            "deviceNum": scene.deviceNumber
        }
        ret.get('data').append(sce)
        print(sce)
    return ret

if __name__ == '__main__':
    app.run()
