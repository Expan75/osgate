from queue import Queue
from typing import List
from abc import ABC, abstractmethod
from devices.device import Device
from devices.deviceFactory import create_device

class AbstractConnector(ABC):
    """Abstract base class for connector. A connector is used as the interface between devices and the gateway"""    
    @abstractmethod
    def initialise() -> None:
        pass

    @abstractmethod
    def shutdown() -> None:
        pass
    
    @abstractmethod
    def restart() -> None:
        pass

    @abstractmethod
    def ping() -> str:
        pass

class ConnectorBase():
    """Captures common state for connectors and common boilerplate methods"""
    def __init__(self, name: str, uuid: str, devices: List[Device], queue: Queue, meta: dict):
        self.protocol = "default"
        self.name = name
        self.uuid = uuid
        self.outbound_queue = queue
        self.meta = meta

        device_types = [device.pop("type") for device in devices]
        self.devices = [create_device(*device) for device in zip(device_types, devices)]
    
    def __str__(self):
        return f"{self.name} ({self.protocol}) - devices={len(self.devices)})"

    def __iter__(self):
        self.__device_index = 0
        return self

    def __next__(self):
        """Allows the [device for device in connnector]"""
        if self.__device_index <= len(self.devices):
            device = self.devices[self.__device_index]
            self.__device_index += 1
            return device
        else:
            raise StopIteration