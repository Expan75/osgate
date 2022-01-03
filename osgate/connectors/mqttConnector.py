import logging
from time import sleep
from queue import Queue
from typing  import List
from threading import Thread
from dataclasses import dataclass
from paho.mqtt import client as mqtt_client

from connectors.connector import Connector
from devices.deviceFactory import create_device

log = logging.getLogger("connector")

@dataclass
class MqttConnectorMetaData():
    host: str = "localhost"
    port: int = 1883
    keep_alive: int = 60

class MqttConnector(Connector):
    """Used for passing data back and forth over mqtt"""
    def __init__(self, name: str, uuid: str, devices: List, queue: Queue, meta: dict):
        self.protocol = "mqtt"
        self.name = name
        self.uuid = uuid
        self.outbound_queue = queue
        self.client = mqtt_client.Client()
        self.connector_meta = MqttConnectorMetaData(**meta)
        
        device_types = [device.pop("type") for device in devices]
        self.devices = [create_device(*device) for device in zip(device_types, devices)]

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

    def __str__(self):
        return f"{self.name} ({self.protocol}Connector) - {self.uuid} - devices={len(self.devices)})"