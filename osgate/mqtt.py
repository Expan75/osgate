import logging
from paho.mqtt import client as mqtt_client
from threading import Thread
from time import sleep

log = logging.getLogger(__name__)

class MqttClient(Thread):
    pass

# 1. start with two distinct topics
# 2. listen to each one with two distinct clients
# 3. have them run concurrently
# 4. have each client publish to the opposite topic
# 5. have each client react to publishes on the "home" topic via subscription/callback
# 6. $$$

if __name__ == '__main__':
    while True:
        print("mqtt in a couple of seconds...")
        sleep(2)