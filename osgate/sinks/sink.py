from abc import ABC, abstractmethod
from queue import Queue
from threading import Thread

class AbstractSink(ABC):
    """Used to represent a final 'place' that data gets sent to, e.g. local file, remote storage, or MQTT broker."""
    @abstractmethod
    def flush() -> None:
        pass
    
    @abstractmethod
    def run() -> None:
        pass

class SinkBase(Thread):
    """Captures common state for data sinks and common boilerplate methods"""
    def __init__(self, queue: Queue, meta: dict):
        Thread.__init__(self, daemon=True)
        self.meta = meta
        self.queue = queue

    def __str__(self):
        return f"Sink:{self.queue}"