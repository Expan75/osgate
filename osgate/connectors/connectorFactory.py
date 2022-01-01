from .defaultConnector import DefaultConnector

def create_connector(protocol: str, connector_data: dict):
    """Factory for creating new connectors"""
    match protocol:
        case "default":
            return DefaultConnector(
                name = connector_data["name"],
                uuid = connector_data["uuid"],
                devices = connector_data["devices"],
                queue = connector_data["queue"],
            )
        case _:
            raise ValueError(f"No connector of protocol {protocol} exists! Perhaps there's a typo in the config.")