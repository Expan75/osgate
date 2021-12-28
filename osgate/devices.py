from abc import ABC

class Device(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def ping() -> str:
        pass

    def ingest() -> str:
        pass

class BaseDevice(Device):
    protocol = "base"
    ingestion = "pull"
    
    def __init__(self, name: str, uuid: str):
        self.name = name
        self.uuid = uuid
     
    def ping() -> str:
        pass