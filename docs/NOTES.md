

## Architecture Plan

1. Everything revolves around a MQTT bridge to either GCP or AWS.
2. Configuration management is YAML file-based but also goes through the bridge.
3. Support both push (mqtt, zwave?) and pull (Mbus, modbus, http) telemetry sources.

## Minor notes

Hierachy-wise, adopt data source pattern

        source1
        |---mqtt-device1
        |---mqtt-device2
        source2
        |---mqtt-device3
        source3
        |---mbus-device1
        |---mbus-device2
        |---mbus-device3

Lifecycle of data sources