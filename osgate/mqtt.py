import logging
from paho.mqtt import client as mqtt_client
from threading import Thread
from time import sleep
from dataclasses import dataclass
from typing import Callable, List

log = logging.getLogger(__name__)

@dataclass
class MqttConnectionDetails():
    host: str = "localhost"
    port: int = 1883
    keep_alive: int = 60

class MqttClient(Thread):
    def __init__(self, details: MqttConnectionDetails, source_topic: str, target_topic="export"):
        self.client = mqtt_client.Client().connect(details.host, details.port, details.keep_alive)
        self.subscribe()

    def subscribe_to_topics(self, topics=List[str]):
        for topic in topics:
            self.client.subscribe(topic)
            log.debug("mqtt client subscribed to {topic}")

    def register_callback(self, topic: str, callable: Callable):
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