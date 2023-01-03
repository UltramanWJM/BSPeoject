import paho.mqtt.client as mqtt
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:8922298@localhost:3306/bs", encoding="utf-8")
# 格式说明：数据库类型 + 数据库驱动器://用户名:密码@地址:端口/数据库名
Session = sessionmaker(bind=engine)
session = Session()

# MQTT Settings
MQTT_Broker = "127.0.0.1"
MQTT_Port = 1883
Keep_Alive_Interval = 80
MQTT_Topic = "bsclient"

def on_connect(client, userdata, flags, rc):
    print("连接")
    print("Connected with result code: " + str(rc))

def on_message(client, userdatam, msg):
    print("消息内容")
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
client.loop_forever()