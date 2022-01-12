import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

log = logging.getLogger(__name__)

@dataclass
class DeviceChannel():
    """Used to denote a unique timeseries source on a device; e.g. kw/h readings from a sensor"""
    name: str
    unit: str
    interval: str

class Device(ABC):
    """Used to represnt a physical entity that produces, and potentially consumes data. Think sensor.""" 
    name: str
    uuid: str
    channels: list[DeviceChannel]
    device_meta: dict

    @abstractmethod
    def ping() -> str:
        pass