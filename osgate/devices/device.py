import logging
from datetime import datetime, timedelta
from dataclasses import dataclass

log = logging.getLogger(__name__)

@dataclass
class DeviceChannel():
    """Used to denote a unique timeseries source on a device; e.g. kw/h readings from a sensor"""
    name: str
    unit: str
    interval: str

    def __post_init__(self):
        pass

    def parse_interval_string(interval: str) -> timedelta:
        pass
    
@dataclass
class Device():
    """Used to represnt a physical entity that produces, and potentially consumes data. Think sensor.""" 
    name: str
    uuid: str
    channels: list[DeviceChannel]
    device_meta: dict

class DefaultDevice(Device):
    """Implments a basic device which can be uniquely identified"""
    type = "default"