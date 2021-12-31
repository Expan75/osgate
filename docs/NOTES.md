

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

What's the point of this?
- Every data source will require a different connector.
- Connectors need to run concurrently. (threads)

Goals:
1. Allow data gathering from at least two different MQTT brokers. (fake it for now using two seperate connections to different topics)
2. Each "module" is responsible for sending data into a single topic. Main thread may opt for final processing before shipping to export topic.

# Architecture

## Something about services
- GatewayService: in charge of everything, effectively a RPC server
- ConfigurationService: handles configuration. Is a dependency everywhere.
- MqttInternalService: in charge of translating local broker events into jsonrpc and vice versa (delegates back and from GatewayService).
- MqttExternalService: in charge of communicating with external brokers, mostly for consumption of data published to other brokers.