from abc import ABC, abstractmethod, property
from dataclasses import dataclass

class DeviceSource(ABC):
    """Abstract BaseClass for potential "parent" of many devices (DeviceSource); e.g. sensor1 and sensor2 from the same MQTT broker"""
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def uuid(self):
        pass

    @abstractmethod
    def connect() -> str:
        """start of lifecycle"""
        # EXAMPLES:
        # 1. connect to MQTT broker
        # 2. Initalise zwave dependency and load driver instance
        # 3. Verify we can connect to serial port (MBUS/MODBUS)
        pass

    @abstractmethod
    def disconnect() -> str:
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
    protocol: str = "default"
    ingestion: str = "pull"
     
    def ping() -> str:
        return "pong"

    def ingest() -> None:
        print("something was ingested.")