import pytest
from osgate.connectors import connectorFactory

def test_valid_connector_creation():
  connector = connectorFactory.create_connector({
    "protocol": "default",
    "name": "Kontor server",
    "uuid": "06660949-eda8-4535-b96f-0d339562a26c",
    "meta": { "somekey" : "somevalue" },
    "devices": []
  })
  assert(connector.type == "default")
  assert(len(connector.devices) == 0)

def test_invalid_connector_creation():
  assert(True)