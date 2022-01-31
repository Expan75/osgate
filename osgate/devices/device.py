import logging
from typing import List
from datetime import timedelta
from dataclasses import dataclass

log = logging.getLogger(__name__)


@dataclass
class DeviceChannel:
    """Used to denote a unique timeseries source on a device; e.g. kw/h readings from a sensor. Interval is given in seconds."""

    name: str
    unit: str
    interval: int

    def __post_init__(self):
        self.interval_timedelta = timedelta(seconds=self.interval)


@dataclass
class Device:
    """Used to represnt a physical entity that produces, and potentially consumes data. Think sensor."""

    name: str
    uuid: str
    channels: List[DeviceChannel]
    device_meta: dict


class DefaultDevice(Device):
    """Implments a basic device which can be uniquely identified"""

    type = "default"
