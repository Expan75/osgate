from typing import List
from devices.device import Device, DeviceChannel

class DefaultDevice(Device):
    def __init__(self, name: str, uuid: str, channels: List[DeviceChannel]):
        self.name = name
        self.uuid = uuid
        self.channels = channels

    def ping() -> str:
        return "pong"