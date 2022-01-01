import logging
from queue import Queue
from typing import List
from threading import Thread
from abc import ABC, abstractmethod
from devices.device import Device

log = logging.getLogger(__name__)

class Connector(ABC):
    """In charge of facilitating communication between gatewayService and devices"""
    name: str
    uuid: str
    protocol: str
    outbound_queue: Queue
    devices: List[Device]

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