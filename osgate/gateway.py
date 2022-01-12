import logging
from queue import Queue
from configuration import ConfigurationService
from connectors.connectorFactory import create_connector

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

log = logging.getLogger(__name__)

class GatewayService():
	"""Gateway driver: in charge of initalizing dependencies and message traffic (operates as singleton web server)"""
	def __init__(self, configService: ConfigurationService):
		self.queue = Queue(0)
		self.configurationService = configService
		self.connectors = self.setup_connectors()

	def setup_connectors(self):
		log.debug("Loading connectors")
		connectors = self.configurationService.config["connectors"]
		loaded_connectors = []
		for connector_data in connectors:
			protocol = connector_data.pop("protocol")
			connector_data["queue"] = self.queue
			connector = create_connector(protocol, connector_data)
			loaded_connectors.append(connector)
		log.debug(f"{len(loaded_connectors)} connectors loaded")
		return loaded_connectors

	def start_connectors(self):
		for connector in self.connectors:
			connector.initialise()

	@Request.application
	def rpc_application(self, request):
		"""Implments the rpc server method handlers"""
		dispatcher["ping"] = lambda: "pong"
		dispatcher["connectors.list"] = lambda: [{"protocol": connector.protocol, "name": connector.name} for connector in self.connectors]

		response = JSONRPCResponseManager.handle(
			request.data, dispatcher)
		return Response(response.json, mimetype='application/json')

	def run(self):
		log.info(f"GatewayService fully initalised, starting device collection using {len(self.connectors)} connectors")
		self.start_connectors()
		run_simple("localhost", 9090, self.rpc_application)