import random
import paho.mqtt.client as mqtt
import time

broker = 'broker.emqx.io'
client = mqtt.Client("HMI for robot control")
client.connect(broker)

def publish(msg):
    client.publish("commands", msg)
    print("publish_" + msg + "_now")
    time.sleep(1)

