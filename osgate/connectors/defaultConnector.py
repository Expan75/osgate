import time
import logging

from connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)

class DefaultConnector(AbstractConnector, ConnectorBase):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data"""
    protocol = "default"

    def run(self) -> None:
        while True:
            log.debug(f"{self} connector running, brum brum...")
            time.sleep(2)
    
    def stop(self) -> None:
        log.debug(f"shutting down {self}...")
        exit()

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"