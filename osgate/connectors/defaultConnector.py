import time
import random
import logging
from datetime import datetime
from connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)

class DefaultConnector(AbstractConnector, ConnectorBase):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data.
       Emulates polling of some devices at given interval (based of osgate.json config). 
    """
    protocol = "default"
    last_seen = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for device in self.devices:
            for channel in device.channels:
                identifer = ".".join((device.uuid, channel.unit))
                self.last_seen[identifer] = datetime.now()

    def poll(self):
        """Polls devices via their channels if last poll was outside of the provided interval"""
        for device in self.devices:
            for channel in device.channels:
                value = random.randint(0,255)
                log.debug(f"ValueChanged Event from {device}, {value=}", {channel.unit})
                identifer = ".".join((device.uuid, channel.unit))
                self.last_seen[identifer] = datetime.now()

    def run(self):
        log.debug(f"{self} starting polling")
        while True:
            time.sleep(0.2)
            self.poll()

    def stop(self):
        log.debug(f"shutting down {self}...")
        exit()

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"