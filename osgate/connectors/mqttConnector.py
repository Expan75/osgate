import logging
from dataclasses import dataclass
from paho.mqtt import client as mqtt_client

from osgate.connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)


@dataclass
class MqttConnectionDetails:
    host: str
    port: int
    keepalive: int


class MqttConnector(AbstractConnector, ConnectorBase):
    """Used to interact with devices through an MQTT broker"""

    protocol = "mqtt"
    client = mqtt_client.Client()

    def run(self):
        log.debug(f"starting {self}...")
        self.register_handlers()
        self.connect()
        self.client.loop_forever()

    def stop(self):
        log.debug(f"shutting down {self}...")
        exit()

    def connect(self):
        mqtt_details = MqttConnectionDetails(**self.meta)
        self.client.connect(
            host=mqtt_details.host,
            port=mqtt_details.port,
            keepalive=mqtt_details.keepalive,
        )

    def on_connect(self, client, userdata, flags, rc):
        """Callback on connection. Ensures subcription is redone if connection is re-established"""
        log.debug("Connected with result code " + str(rc))
        client.subscribe("$SYS/#")

    def on_message(self, client, userdata, message):
        """General callback upon message to topics currently being subscribed too"""
        log.debug(
            f"{self} recived message from {message.topic} /w payload: {str(message.payload)}"
        )

    def register_handlers(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"
