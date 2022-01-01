from devices.device import Device, DeviceChannel
from typing import List

class DefaultDevice(Device):
    def __init__(self, name: str, uuid: str, channels: List[DeviceChannel]):
        self.name = name
        self.uuid = uuid
        self.channels = channels

    def ping() -> str:
        return "pong"