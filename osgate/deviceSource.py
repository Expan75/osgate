import logging
from typing import List
from dataclasses import dataclass
from abc import ABC, abstractmethod
from devices import Device, create_device

log = logging.getLogger(__name__)

class DeviceSource(ABC):
    """Abstract BaseClass for potential "parent" of many devices (DeviceSource); e.g. sensor1 and sensor2 from the same MQTT broker"""
    @abstractmethod
    def initalise() -> str:
        """start of lifecycle"""
        # EXAMPLES:
        # 1. connect to MQTT broker
        # 2. Initalise zwave dependency and load driver instance
        # 3. Verify we can connect to serial port (MBUS/MODBUS)
        pass

    @abstractmethod
    def remove() -> str:
        """end of lifecycle"""
        # EXAMPLES:
        # 1. disconnect from MQTT broker
        # 2. Shut down zwave gracefully
        # 3. Give up serial port (MBUS/MODBUS)
        pass

    @abstractmethod
    def ping() -> str:
        pass

@dataclass
class DefaultDeviceSource(DeviceSource):
    """Default deviceSouce; used for debugging and experimentation"""
    name: str
    uuid: str
    devices: List[Device]
    protocol: str = "default"

    def initalise(self) -> str:
        log.debug(f"DefaultDeviceSource: {id(self)} initalised successfully.")
        "print"
    
    def remove(self) -> str:
        log.debug(f"DefaultDeviceSource: {id(self)} removed successfully.")
        "print"

    def ping(self) -> str:
        return "pong"

def create_device_source(protocol, name, uuid, devices):
    devices = [create_device(device["name"], device["uuid"], device_type="default") for device in devices]
    match protocol:
        case _:        
            return DefaultDeviceSource(name=name, uuid=uuid, devices=devices)