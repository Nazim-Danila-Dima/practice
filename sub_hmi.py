import random
import time

from paho.mqtt import client as mqtt_client

mess = " "
broker = 'broker.emqx.io'
port = 1883
topic = "hmi_pub"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'NDD55'
password = 'NDD55'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    global mess
    mess = msg.payload.decode()



def run():
    client = connect_mqtt()
    client.loop_start()
    client.subscribe(topic)
    client.on_message = on_message
    time.sleep(3)




