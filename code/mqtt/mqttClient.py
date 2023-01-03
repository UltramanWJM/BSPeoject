import paho.mqtt.client as mqtt

# MQTT Settings
MQTT_Broker = "127.0.0.1"
MQTT_Port = 1883
Keep_Alive_Interval = 80
MQTT_Topic = "bsclient"

def on_connect(client, userdata, flags, rc):
    print("Connect with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
# send format: deviceId#info0-info1-info2#valid
# Light info： luminance
# Lock info： status
# Sensor info: temperature-humidity

send = ''
# client.publish(MQTT_Topic, payload='21#3#1', qos=0) # light

# client.publish(MQTT_Topic, payload='23#24-15#1', qos=0) # sensor
client.publish(MQTT_Topic, payload='26#1#1', qos=0) # lock