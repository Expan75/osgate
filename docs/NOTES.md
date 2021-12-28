

## Architecture Plan

1. Everything revolves around a MQTT bridge to either GCP or AWS.
2. Configuration management is YAML file-based but also goes through the bridge.
3. Support both push (mqtt, zwave?) and pull (Mbus, modbus, http) telemetry sources.