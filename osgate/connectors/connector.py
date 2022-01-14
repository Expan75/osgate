from queue import Queue
from typing import List
from abc import ABC, abstractmethod
from threading import Thread

from devices.deviceFactory import create_device

class AbstractConnector(ABC):
    """Abstract base class for connector. A connector is used as the interface between devices and the gateway"""    
    @abstractmethod
    def run() -> None:
        pass

    @abstractmethod
    def stop() -> None:
        pass

    @abstractmethod
    def ping() -> str:
        pass

class ConnectorBase(Thread):
    """Captures common state for connectors and common boilerplate methods"""
    def __init__(self, name: str, uuid: str, devices: List, queue: Queue, meta: dict):
        Thread.__init__(self, daemon=True)
        self.name = name
        self.uuid = uuid
        self.outbound_queue = queue
        self.meta = meta

        device_types = [device.pop("type") for device in devices]
        self.devices = [create_device(*device) for device in zip(device_types, devices)]
    
    def __str__(self):
        return f"{self.name} ({self.protocol}) - devices={len(self.devices)})"

    def __iter__(self):
        """Enables looping over devices"""
        return iter(self.devices)