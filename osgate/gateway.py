import logging
from queue import Queue
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from configuration import ConfigurationService
from connectors import connectorFactory
from sinks import sinkFactory

log = logging.getLogger(__name__)


class GatewayService:
    """Gateway driver: in charge of initalizing dependencies and delegating based off jsonrpc requests"""

    def __init__(self, configService: ConfigurationService):
        self.queue = Queue(0)
        self.configurationService = configService
        self.sinks = []
        self.connectors = []

        self.load_sinks()
        self.load_connectors()

    def load_sinks(self):
        """Initalises the data sinks that will be the final destination of sourced data"""
        sinks = self.configurationService.config["sinks"]
        for sink_data in sinks:
            sink_data["queue"] = Queue()
            sink = sinkFactory.create_sink(sink_data)
            self.sinks.append(sink)
        log.debug(f"{len(self.connectors)} sinks loaded")

    def load_connectors(self):
        """Initalises connector instances based off config; can be used to reload and reflect changed config state"""
        connectors = self.configurationService.config["connectors"]
        for connector_data in connectors:
            connector_data["sinks"] = self.sinks
            connector = connectorFactory.create_connector(connector_data)
            self.connectors.append(connector)
        log.debug(f"{len(self.connectors)} connectors loaded")

    def list_devices(self, connector_name: str) -> list:
        """List devices of a connector (requires a name)"""
        connector = [
            connector
            for connector in self.connectors
            if connector.name == connector_name
        ]
        return [device.name for device in connector[0]] if connector else []

    def start_connectors(self):
        """Starts a background thread for each connector"""
        for connector in self.connectors:
            connector.start()

    def stop_connectors(self):
        """Gracefully stops the background thread for each connector"""
        for connector in self.connectors:
            connector.stop()

    def restart_connectors(self):
        """Gracefully reloads the configuration and restarts the background thread for each connector"""
        self.stop_connectors()
        self.load_connectors()
        self.start_connectors()

    def run(self):
        self.start_connectors()
        log.info(f"Connectors started, starting jsonrpc server...")
        run_simple("localhost", 9090, self.rpc_application)

    # TODO: encapsulate the RPC better
    @Request.application
    def rpc_application(self, request):
        """Implments the rpc server method handlers"""
        dispatcher["ping"] = lambda: "pong"
        dispatcher["devices.list"] = lambda connector_name: self.list_devices(
            connector_name
        )
        dispatcher["connectors.list"] = lambda: [
            {"protocol": connector.protocol, "name": connector.name}
            for connector in self.connectors
        ]

        response = JSONRPCResponseManager.handle(request.data, dispatcher)
        return Response(response.json, mimetype="application/json")
