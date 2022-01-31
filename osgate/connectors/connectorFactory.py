import logging

from connectors.defaultConnector import DefaultConnector
from connectors.mqttConnector import MqttConnector
from sinks.sink import AbstractSink

log = logging.getLogger(__name__)


def create_connector(connector_data: dict):
    """Factory for creating new connectors"""
    protocol = connector_data.get("protocol")
    name = connector_data.get("name")
    uuid = connector_data.get("uuid")
    devices = connector_data.get("devices")
    sinks = connector_data.get("sinks")
    connector_metadata = connector_data.get("meta")

    log.debug(
        f"creating connector /w protocol {protocol} using data: {connector_data=}"
    )
    # fmt: off
    match protocol:
        case "default":
            return DefaultConnector(name, uuid, devices, sinks, connector_metadata)
        case "mqtt":
            return MqttConnector(name, uuid, devices, sinks, connector_metadata)
        case _:
            raise NotImplementedError(
                f"No connector of protocol {protocol} exists! Perhaps there's a typo in the config."
            )
    # fmt: on