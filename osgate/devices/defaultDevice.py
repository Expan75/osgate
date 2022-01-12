from typing import List, Optional
from devices.device import Device, DeviceChannel

class DefaultDevice(Device):
    """Implments a basic device which can be uniquely identified"""
    def __init__(self, name: str, uuid: str, channels: List[DeviceChannel], meta: Optional[dict]):
        self.name = name
        self.uuid = uuid
        self.channels = channels
        self.meta = meta

    def ping() -> str:
        return "pong"