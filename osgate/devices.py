from abc import ABC, abstractmethod
from dataclasses import dataclass

class Device(ABC):
    def __init__(self, name: str, uuid: str, *args, **kwargs):
        pass

    @abstractmethod
    def ping() -> str:
        pass

    @abstractmethod
    def ingest() -> None:
        pass

@dataclass
class BaseDevice(Device):
    protocol: str = "base"
    ingestion: str = "pull"
     
    def ping() -> str:
        return "pong"

    def ingest() -> None:
        print("something was ingested.")