from devices.device import Device
from devices.defaultDevice import DefaultDevice

def create_device(_type, *args) -> Device:
    match _type:
        case _:        
            return DefaultDevice(*args)