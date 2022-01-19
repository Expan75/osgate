import time
import logging
import random
from dataclasses import dataclass
from connectors.connector import AbstractConnector, ConnectorBase

log = logging.getLogger(__name__)

class DefaultConnector(AbstractConnector, ConnectorBase):
    """Used for testing of design pattern; allows non-existing connector and devices to be source of data.
       Emulates polling of some devices at given interval (based of osgate.json config). 
    """
    protocol = "default"
    last_polled = {} # device_uuid.channel.name : datetime.datetime

    def poll(self):
        """Polls devices via their channels if last poll was outside of the provided interval"""
        for device in self.devices:
            for channel in device.channels:
                value = random.randint(0, 255)
                log.debug(f"{device.name} generated value {value} {channel.unit} from channel: {channel.name}")

                # how to handle poll timers? Refactor device channel? Timedelta?

    def run(self):
        while True:
            log.debug(f"{self} connector running, brum brum...")            
            time.sleep(1)

    def stop(self):
        log.debug(f"shutting down {self}...")
        exit()

    def ping(self) -> str:
        log.debug(f"send ping to connector: {self.name}")
        return "pong"

    def parse_interval_string(interval: str) -> int:
        """Parses an interval string, e.g. '60s' to the corresponding milliseconds in python"""
        return 1000