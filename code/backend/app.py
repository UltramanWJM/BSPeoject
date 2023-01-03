import json

from flask import Flask, jsonify, request, flash, send_file, make_response
from flask_cors import CORS
from initDatabase import createApp
from initDatabase import db
from models import Users, Scenes, Devices, Lights, Lockes, Sensors, Switches, DeviceMes
import os, random, io
from PIL import Image
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
    rad = random.randrange(0, 1000)
    i = imgName.index('.')
    filePath = path + imgName[0:i] + str(rad) + imgName[i:]
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

@app.route('/deletescene', methods=['POST', 'GET'])
def deleteScene():
    data = request_parse(request)
    sceneId = data.get('sceneId')
    scenes = Scenes.query.filter(Scenes.sceneId == sceneId).all()
    for scene in scenes:
        path = scene.imgPath
        os.remove(path)
        db.session.delete(scene)
    db.session.commit()
    return jsonify(code=1, msg="删除场景成功！")

@app.route('/getsceneimg', methods=['GET', 'POST'])
def getSceneImg():
    data = request_parse(request)
    sceneId = data.get('sceneId')
    scene = Scenes.query.filter(Scenes.sceneId == sceneId).first()
    path = scene.imgPath
    imageData = open(path, "rb").read()
    # res = make_response(imageData)
    # res.headers['Content-Type'] = 'image/png'
    imgStream = io.BytesIO(imageData)
    img = Image.open(imgStream)
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

@app.route('/getcreatedscenes', methods=['GET'])
def getCreatedScenes():
    data = request_parse(request)
    userId = data.get('userId')
    scenes = Scenes.query.filter(Scenes.userId == userId).all()
    ret = {
        "code": 1,
        "data": []
    }
    for scene in scenes:
        sce = {
            "value": scene.sceneId,
            "label": scene.sceneName
        }
        ret.get('data').append(sce)
        print(sce)
    return ret

@app.route('/getdevices', methods=['GET', 'POST'])
def getDevices():
    data = request_parse(request)
    userId = data.get('userId')
    devices = Devices.query.filter(Devices.userId == userId).all()
    ret = {
        "code": 1,
        "data": []
    }
    for device in devices:
        dT = '啥也不是' # dT: device type
        if device.deviceType == 0:
            dT = "灯"
        elif device.deviceType == 1:
            dT = "开关"
        elif device.deviceType == 2:
            dT = "传感器"
        elif device.deviceType == 3:
            dT = "门锁"
        dev = {
            "deviceId": device.deviceId,
            "deviceName": device.deviceName,
            "deviceType": dT,
            "sceneId": device.sceneId
        }
        ret.get('data').append(dev)
        print(dev)
    return ret

@app.route('/deletedevice', methods=['POST', 'GET'])
def deleteDevice():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    devices = Devices.query.filter(Devices.deviceId == deviceId).all()
    for device in devices:
        db.session.delete(device)
    db.session.commit()
    return jsonify(code=1, msg="删除设备成功！")

@app.route('/createdevice', methods=['GET', 'POST'])
def createDevice():
    data = request_parse(request)
    deviceId = data.get('newDeviceId')
    deviceName = data.get('newDeviceName')
    userId = data.get('userId')
    deviceType = data.get('newDeviceType')
    sceneId = data.get('newDeviceScene')
    positionX = data.get('newDevicePX')
    positionY = data.get('newDevicePY')
    devices = Devices.query.filter(Devices.deviceId == deviceId).all()
    res = {
        "code": 1,
        "msg": ""
    }
    if (devices):
        res["code"] = 0
        res["msg"] = "Already exist DeviceID " + sceneId
        return res
    newDevice = Devices(deviceId=deviceId, deviceName=deviceName, userId=userId, sceneId=sceneId, deviceType=deviceType, positionX=positionX, positionY=positionY)
    db.session.add(newDevice)
    scene = Scenes.query.filter(Scenes.sceneId == sceneId).first()
    scene.deviceNumber = scene.deviceNumber + 1
    if deviceType == 0: # 灯
        newLight = Lights(deviceId=deviceId, status=0, luminance=0)
        newLightInfo = DeviceMes(deviceId=deviceId, info='', valid=0)
        db.session.add(newLight)
        db.session.add(newLightInfo)
    elif deviceType == 1: # 开关
        newSwitch = Switches(deviceId=deviceId, status=0)
        newSwitchInfo = DeviceMes(deviceId=deviceId, info='', valid=0)
        db.session.add(newSwitch)
        db.session.add(newSwitchInfo)
    elif deviceType == 2: # 传感器
        newSensor = Sensors(deviceId=deviceId, temperature=0, humidity=0, status=0)
        newSensorInfo = DeviceMes(deviceId=deviceId, info='', valid=0)
        db.session.add(newSensor)
        db.session.add(newSensorInfo)
    elif deviceType == 3: # 门锁
        newLock = Lockes(deviceId=deviceId, status=0)
        newLockInfo = DeviceMes(deviceId=deviceId, info='', valid=0)
        db.session.add(newLock)
        db.session.add(newLockInfo)
    db.session.commit()
    res["msg"] = "新设备创建成功"
    return res

@app.route('/getdevice', methods=['GET', 'POST'])
def getDevice():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    device = Devices.query.filter(Devices.deviceId == deviceId).first()
    res = {
        "code": 1,
        "deviceId": deviceId,
        "positionX": device.positionX,
        "positionY": device.positionY
    }
    return res

@app.route('/getlamps', methods=['GET', 'POST'])
def getLamps():
    data = request_parse(request)
    userId = data.get('userId')
    allLamps = []
    lamps = Devices.query.filter(Devices.userId == userId, Devices.deviceType == 0).all()
    for lamp in lamps:
        temp0 = DeviceMes.query.filter(DeviceMes.deviceId == lamp.deviceId).first()
        temp1 = Lights.query.filter(Lights.deviceId == lamp.deviceId).first()
        if temp0.valid == 1:
            temp1.status = 1
            temp1.luminance = int(temp0.info)
            db.session.commit()
        st = "正常"
        if temp1.status == 0:
            st = "离线"
        lampInfo = {
            "deviceId" : lamp.deviceId,
            "deviceName": lamp.deviceName,
            "luminance": temp1.luminance,
            "status": st,
            "updateTime": temp0.timestamp
        }
        allLamps.append(lampInfo)
    ret = {
        "code": 1,
        "data": allLamps
    }
    return ret

@app.route('/modlampstatus', methods=['GET', 'POST'])
def modLampStatus():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    ret = {
        "msg" : "开启成功",
        "code": 1
    }
    lamp = Lights.query.filter(Lights.deviceId == deviceId).first()
    lampMes = DeviceMes.query.filter(DeviceMes.deviceId == deviceId).first()
    if lamp.status == 0:
        lamp.status = 1
    else:
        lamp.status = 0
        ret["msg"] = "关闭成功"
        lampMes.valid = 0
    db.session.commit()
    return ret

@app.route('/lightenlight', methods=['GET', 'POST'])
def lightenLight():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    ret = {
        "msg" : "调整亮度为",
        "code": 1
    }
    lamp = Lights.query.filter(Lights.deviceId == deviceId).first()
    lampMes = DeviceMes.query.filter(DeviceMes.deviceId == deviceId).first()
    if lamp.luminance == 5:
        ret["msg"] = "已达到最大亮度，无法调亮"
        ret["code"] = 0
    else:
        lamp.luminance = lamp.luminance + 1
        ret["msg"] = "调整亮度为" + str(lamp.luminance)
        lampMes.valid = 0
    db.session.commit()
    return ret

@app.route('/dimlight', methods=['GET', 'POST'])
def dimLight():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    ret = {
        "msg" : "调整亮度为",
        "code": 1
    }
    lamp = Lights.query.filter(Lights.deviceId == deviceId).first()
    lampMes = DeviceMes.query.filter(DeviceMes.deviceId == deviceId).first()
    if lamp.luminance == 1:
        ret["msg"] = "已达到最低亮度，无法调暗"
        ret["code"] = 0
    else:
        lamp.luminance = lamp.luminance - 1
        ret["msg"] = "调整亮度为" + str(lamp.luminance)
        lampMes.valid = 0
    db.session.commit()
    return ret

@app.route('/getlockes', methods=['GET', 'POST'])
def getLockes():
    data = request_parse(request)
    userId = data.get('userId')
    allLockes = []
    lockes = Devices.query.filter(Devices.userId == userId, Devices.deviceType == 3).all()
    for lock in lockes:
        temp0 = DeviceMes.query.filter(DeviceMes.deviceId == lock.deviceId).first()
        temp1 = Lockes.query.filter(Lockes.deviceId == lock.deviceId).first()
        if temp0.valid == 1:
            temp1.status = int(temp0.info)
            # print(temp1.status)
            db.session.commit()
        st = "上锁"
        if temp1.status == 0:
            st = "开锁"
        lockInfo = {
            "deviceId": lock.deviceId,
            "deviceName": lock.deviceName,
            "status": st,
            "updateTime": temp0.timestamp
        }
        allLockes.append(lockInfo)
    ret = {
        "code": 1,
        "data": allLockes
    }
    return ret

@app.route('/modlockstatus', methods=['GET', 'POST'])
def modLockStatus():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    ret = {
        "msg" : "上锁成功",
        "code": 1
    }
    lock = Lockes.query.filter(Lockes.deviceId == deviceId).first()
    lockMes = DeviceMes.query.filter(DeviceMes.deviceId == deviceId).first()
    if lock.status == 0:
        lock.status = 1
        lockMes.valid = 0
    else:
        lock.status = 0
        ret["msg"] = "开锁成功"
        lockMes.valid = 0
    db.session.commit()
    return ret

@app.route('/getswitches', methods=['GET', 'POST'])
def getSwitches():
    data = request_parse(request)
    userId = data.get('userId')
    allSwitches = []
    switches = Devices.query.filter(Devices.userId == userId, Devices.deviceType == 1).all()
    for switch in switches:
        temp0 = DeviceMes.query.filter(DeviceMes.deviceId == switch.deviceId).first()
        temp1 = Switches.query.filter(Switches.deviceId == switch.deviceId).first()
        if temp0.valid == 1:
            temp1.status = int(temp0.info)
            # print(temp1.status)
            db.session.commit()
        st = "开启"
        if temp1.status == 0:
            st = "关闭"
        switchInfo = {
            "deviceId": switch.deviceId,
            "deviceName": switch.deviceName,
            "status": st,
            "updateTime": temp0.timestamp
        }
        allSwitches.append(switchInfo)
    ret = {
        "code": 1,
        "data": allSwitches
    }
    return ret

@app.route('/modswitchstatus', methods=['GET', 'POST'])
def modSwitchStatus():
    data = request_parse(request)
    deviceId = data.get('deviceId')
    ret = {
        "msg" : "开启成功",
        "code": 1
    }
    switch = Switches.query.filter(Switches.deviceId == deviceId).first()
    switchMes = DeviceMes.query.filter(DeviceMes.deviceId == deviceId).first()
    if switch.status == 0:
        switch.status = 1
        switchMes.valid = 0
    else:
        switch.status = 0
        ret["msg"] = "关闭成功"
        switchMes.valid = 0
    db.session.commit()
    return ret

@app.route('/getsensors', methods=['GET', 'POST'])
def getSensors():
    data = request_parse(request)
    userId = data.get('userId')
    allSensors = []
    sensors = Devices.query.filter(Devices.userId == userId, Devices.deviceType == 2).all()
    for sensor in sensors:
        temp0 = DeviceMes.query.filter(DeviceMes.deviceId == sensor.deviceId).first()
        temp1 = Sensors.query.filter(Sensors.deviceId == sensor.deviceId).first()
        if temp0.valid == 1:
            temp1.status = 1
            infos = temp0.info.split("-")
            temp1.temperature = float(infos[0])
            temp1.humidity = float(infos[1])
            db.session.commit()
        st = "在线"
        if temp1.status == 0:
            st = "离线"
        sensorInfo = {
            "deviceId" : sensor.deviceId,
            "deviceName": sensor.deviceName,
            "temperature": temp1.temperature,
            "humidity": temp1.humidity,
            "status": st,
            "updateTime": temp0.timestamp
        }
        allSensors.append(sensorInfo)
    ret = {
        "code": 1,
        "data": allSensors
    }
    return ret

if __name__ == '__main__':
    app.run()
