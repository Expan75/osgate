import logging
from time import sleep
from queue import Queue
from typing  import List

from .connector import Connector
from devices.deviceFactory import create_device

log = logging.getLogger(__name__)

class DefaultConnector(Connector):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data"""
    def __init__(self, name: str, uuid: str, devices: List, queue: Queue):
        self.protocol = "default"
        self.name = name
        self.uuid = uuid
        self.outbound_queue = queue

        device_types = [device.pop("type") for device in devices]
        self.devices = [create_device(*device) for device in zip(device_types, devices)]

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