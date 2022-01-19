from dataclasses import dataclass
from paho.mqtt import client as mqtt_client
from sinks.sink import AbstractSink, SinkBase

@dataclass
class MqttDataSinkConnectionDetails():
    host: str
    port: int
    keepalive: int

class MqttDataSink(AbstractSink, SinkBase):
    """Used to export data to a MQTT broker; designed with the intent of the broker running locally"""
    client = mqtt_client.Client()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mqtt_details = MqttDataSinkConnectionDetails(**self.meta)

    def run():
        pass

    def flush():
        pass