import random

from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "hmi_pub"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'NDD55'
password = 'NDD55'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("коннект с mqtt broker!")
        else:
            print("ошибка соединения %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, msg):
    msg = f"messages: top = {msg}"
    result = client.publish(topic, msg)
    print(f"Send `{msg}` to topic `{topic}`")



def start():
    client = connect_mqtt()
    client.loop_start()
