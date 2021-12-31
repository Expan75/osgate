import logging
from queue import Queue
from time import sleep
from configuration import ConfigurationService
from connectors.connector import create_connector

log = logging.getLogger(__name__)

class GatewayService():
	"""Gateway driver: in charge of initalizing dependencies and message traffic (operates as singleton)"""
	def __init__(self, configService: ConfigurationService):
		self.queue = Queue(0)
		self.configurationService = configService
		self.connectors = self.load_connectors()

	def setup_connectors(self):
		log.info("Loading connectors")
		connectors = self.configurationService.config["connectors"]
		loaded_connectors = [create_connector(*connector) for connector in connectors]
		log.info(f"{len(loaded_connectors)} connectors loaded")
		return loaded_connectors

	def run(self):
		log.info(f"GatewayService fully initalised, starting device collection using {len(self.connectors)} connectors")
		while True:
			sleep(2.0)
			print("...")