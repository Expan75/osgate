import logging
from connector import Connector
from ..devices.device import create_device
from time import sleep

log = logging.getLogger(__name__)

class DefaultConnector(Connector):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data"""
    def __init__(self, name, uuid, outbound_queue, devices):
        self.protocol = "default"
        self.name = name
        self.uuid = uuid
        self.outbound_queue = outbound_queue
        self.devices = [create_device(device) for device in devices]

    def __str__(self):
        return f"Connector({self.name},{self.uuid},devices={len(self.devices)})"

    def initialise(self) -> None:
        log.debug(f"{self} initalised")
    
    def shutdown(self) -> None:
        log.debug(f"shutting down {self}...")
        sleep(2)
        log.debug(f"{self} gracefully shutdown.")
    
    def restart(self) -> None:
        log.debug(f"restarting {self}...")
        self.shutdown()
        self.initialise()

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"