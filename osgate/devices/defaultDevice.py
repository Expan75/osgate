from device import Device, DeviceChannel

class DefaultDevice(Device):
    def __init__(self, name, uuid, channels):
        self.name = name
        self.uuid = uuid
        self.channels = [DeviceChannel(channel) for channel in channels]

    def ping() -> str:
        return "pong"