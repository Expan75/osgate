import logging

from sinks.mqttSink import MqttSink

log = logging.getLogger(__name__)


def create_sink(sink_data: dict):
    """Factory for creating new sinks"""
    sink_type = sink_data.get("type")
    name = sink_data.get("name")
    queue = sink_data.get("queue")
    sink_metadata = sink_data.get("meta")

    log.debug(f"creating sink using data: {sink_data=}")

    # fmt: off
    match sink_type:
        case "mqtt":
            return MqttSink(name, queue, sink_metadata)
        case _:
            raise NotImplementedError(
                f"No sink of {sink_type=} exists! Perhaps there's a typo in the config."
            )
    # fmt: on
