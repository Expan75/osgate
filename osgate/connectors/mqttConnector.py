import time
import logging

from connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)

class MqttConnector(AbstractConnector, ConnectorBase):
    """Used to interact with devices through an MQTT broker"""
    protocol = "mqtt"

    def run(self) -> None:
        while True:
            log.debug(f"{self} connector running, brum brum...")
            time.sleep(2)
    
    def stop(self) -> None:
        log.debug(f"shutting down {self}...")
        time.sleep(2)
        log.debug(f"{self} gracefully shutdown.")

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"