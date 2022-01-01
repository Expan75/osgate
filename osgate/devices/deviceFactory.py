from devices.device import Device
from devices.defaultDevice import DefaultDevice, DeviceChannel

def create_device_channel(channel: dict) -> DeviceChannel:
    print(f"{channel=}", )
    return DeviceChannel(
        name = channel.get('name'),
        unit = channel.get('unit'),
        interval = channel.get('interval'),
    )

def create_device(device_type: str, device_data: dict) -> Device:
    match device_type:
        case "sensor":        
            return DefaultDevice(
                name = device_data.get("name"),
                uuid = device_data.get("uuid"),
                channels = [create_device_channel(channel) for channel in device_data.get("channels")],
            )
        case _:
            raise ValueError(f"Invalid device type: {device_type}; perhaps there's a typo in the config file.")