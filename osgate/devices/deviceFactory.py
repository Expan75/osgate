import logging

from devices.device import Device, DefaultDevice, DeviceChannel

log = logging.getLogger(__name__)


def create_device_channel(channel: dict) -> DeviceChannel:
    return DeviceChannel(
        name=channel.get("name"),
        unit=channel.get("unit"),
        interval=channel.get("interval"),
    )


def create_device(device_type: str, device_data: dict) -> Device:
    log.debug(f"creating device /w type {device_type} using data: {device_data=}")
    name = device_data.get("name")
    uuid = device_data.get("uuid")
    meta = device_data.get("meta")
    channels = [
        create_device_channel(channel) for channel in device_data.get("channels")
    ]

    match device_type:
        case "default":
            return DefaultDevice(name, uuid, channels, meta)
        case _:
            raise NotImplementedError(
                f"Invalid device type: {device_type}; perhaps there's a typo in the config file."
            )
