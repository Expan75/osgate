import time
import logging

from connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)

class DefaultConnector(AbstractConnector, ConnectorBase):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data"""
    def initialise(self) -> None:
        log.debug(f"{self} initalised")
    
    def shutdown(self) -> None:
        log.debug(f"shutting down {self}...")
        time.sleep(2)
        log.debug(f"{self} gracefully shutdown.")
    
    def restart(self) -> None:
        log.debug(f"restarting {self}...")
        self.shutdown()
        self.initialise()

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"