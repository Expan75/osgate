import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

log = logging.getLogger(__name__)

class Device(ABC):
    @abstractmethod
    def ping() -> str:
        pass

@dataclass
class DefaultDevice(Device):
    name: str = ""
    uuid: str = ""

    def ping() -> str:
        return "pong"

def create_device(name, uuid, device_type=None):
    match device_type:
        case _:        
            return DefaultDevice(name=name, uuid=uuid)