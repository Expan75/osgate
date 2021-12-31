from .defaultConnector import DefaultConnector

def create_connector(protocol, *args):
    """Factory for creating new connectors"""
    match protocol:
        case "default":        
            return DefaultConnector(*args)
        case _:
            raise ValueError(f"No device of protocol {protocol} exists! Perhaps there's a typo in the config.")