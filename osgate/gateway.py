import logging
from queue import Queue
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from configuration import ConfigurationService
from connectors.connectorFactory import create_connector

log = logging.getLogger(__name__)

class GatewayService():
	"""Gateway driver: in charge of initalizing dependencies and message traffic (operates as singleton web server)"""
	def __init__(self, configService: ConfigurationService):
		self.queue = Queue(0)
		self.configurationService = configService
		self.load_connectors()

	def load_connectors(self):
		"""Initalises connector instances based off config; can be used to reload and reflect changed config state"""
		log.debug("Loading connectors")
		connectors = self.configurationService.config["connectors"]
		loaded_connectors = []
		for connector_data in connectors:
			protocol = connector_data.pop("protocol")
			connector_data["queue"] = self.queue
			connector = create_connector(protocol, connector_data)
			loaded_connectors.append(connector)
		self.connectors = loaded_connectors
		log.debug(f"{len(loaded_connectors)} connectors loaded")


	def list_devices(self, connector_name: str) -> list:
		"""List devices of a connector (requires a name)"""
		connector = [connector for connector in self.connectors if connector.name == connector_name]
		return [device.name for device in connector[0]] if connector else []

	@Request.application
	def rpc_application(self, request):
		"""Implments the rpc server method handlers"""
		dispatcher["ping"] = lambda: "pong"
		dispatcher["connectors.list"] = lambda: [{"protocol": connector.protocol, "name": connector.name} for connector in self.connectors]
		dispatcher["devices.list"] = lambda connector_name: self.list_devices(connector_name)

		response = JSONRPCResponseManager.handle(
			request.data, dispatcher)
		return Response(response.json, mimetype='application/json')
	
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
		log.info(f"GatewayService fully initalised, starting device collection using {len(self.connectors)} connectors")
		self.start_connectors()
		run_simple("localhost", 9090, self.rpc_application)