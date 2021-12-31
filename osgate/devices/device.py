import logging
from abc import ABC, abstractmethod
from defaultDevice import DefaultDevice
from dataclasses import dataclass

log = logging.getLogger(__name__)

@dataclass
class DeviceChannel():
    """Used to denote a unique timeseries source on a device; e.g. kw/h readings from a sensor"""
    name: str
    unit: str

class Device(ABC):
    name: str
    uuid: str
    channels: list[DeviceChannel]

    @abstractmethod
    def ping() -> str:
        pass

def create_device(*args, **kwargs):
    log.debug(f"""creating {kwargs["device_type"]} device with args: {args}""")
    match kwargs["device_type"]:
        case _:        
            return DefaultDevice(*args)