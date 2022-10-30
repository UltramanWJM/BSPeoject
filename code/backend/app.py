import json

from flask import Flask, jsonify, request, flash
from flask_cors import CORS
from initDatabase import createApp
from initDatabase import db
from models import Users
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
    username = data.get('username')
    pwd = data.get('password')
    user = Users.query.filter(Users.username == username, Users.password == pwd).first()
    if user:
        msg = "登陆成功"
        code = 1
    else:
        msg = "登录失败"
        code = 0
    return jsonify(code = code, msg = msg)


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

if __name__ == '__main__':
    app.run()
