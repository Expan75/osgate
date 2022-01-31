import json
import time
import logging
from dataclasses import dataclass
from paho.mqtt import client as mqtt_client
from sinks.sink import AbstractSink, SinkBase

log = logging.getLogger(__name__)

@dataclass
class MqttSinkConfiguration():
    host: str
    port: int
    topic: str
    keepalive: int

class MqttSink(AbstractSink, SinkBase):
    """Used to export data to a MQTT broker; designed with the intent of the broker running locally"""
    client = mqtt_client.Client()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = MqttSinkConfiguration(**self.meta)

    def flush(self, event: dict):
        payload = json.dumps(event)
        log.debug(f"MqttSink Flushing {event=} in topic {self.config.topic}")
        self.client.connect(self.config.host, self.config.port)
        self.client.publish(self.config.topic, payload=payload)
        self.client.disconnect()

    def stop(self):
        log.debug(f"shutting down {self}...")
        exit()

    def run(self):
        while True:
            if self.queue.qsize() != 0:
                event = self.queue.get()
                self.flush(event)
                self.queue.task_done()
            else:
                time.sleep(0.2)