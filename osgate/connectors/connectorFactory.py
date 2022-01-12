import logging

from connectors.defaultConnector import DefaultConnector
from connectors.mqttConnector import MqttConnector

log = logging.getLogger(__name__)

def create_connector(protocol: str, connector_data: dict):
    """Factory for creating new connectors"""
    log.debug(f"creating connector /w protocol {protocol} using data: {connector_data=}")
    name                = connector_data["name"]
    uuid                = connector_data["uuid"]
    devices             = connector_data["devices"]
    queue               = connector_data["queue"]
    connector_metadata  = connector_data["meta"]

    match protocol:
        case "default": return DefaultConnector(name, uuid, devices, queue, connector_metadata)
        case "mqtt": return MqttConnector(name, uuid, devices, queue, connector_metadata)
        case _: raise NotImplementedError(f"No connector of protocol {protocol} exists! Perhaps there's a typo in the config.")