import paho.mqtt.client as mqtt
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

engine = create_engine("mysql+pymysql://root:8922298@localhost:3306/bs", encoding="utf-8")
# 格式说明：数据库类型 + 数据库驱动器://用户名:密码@地址:端口/数据库名
Session = sessionmaker(bind=engine)
session = Session()

# MQTT Settings
MQTT_Broker = "127.0.0.1"
MQTT_Port = 1883
Keep_Alive_Interval = 600
MQTT_Topic = "bsclient"

def on_connect(client, userdata, flags, rc):
    print("连接")
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print("消息内容")
    print(msg.topic + " " + str(msg.payload))
    var = str(msg.payload.decode("utf-8"))
    # send format: deviceId#info0-info1-info2#valid
    total = var.split("#")
    devId = int(total[0])
    info = total[1]
    valid = int(total[2])
    # print(devId)
    # print(info)
    # print(valid)
    stmt1 = f'insert into DeviceMes(deviceID, info, valid) values ("{devId}", "{info}", "{valid}")'
    stmt = f'update DeviceMes set info = "{info}", valid = "{valid}" where deviceID = "{devId}"'
    session.execute(stmt)
    session.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
client.subscribe(MQTT_Topic, qos=0)
client.loop_forever()