import logging
from time import sleep
from conf import ConfigurationService
from deviceSource import create_device_source

log = logging.getLogger(__name__)

class GatewayService():
	def __init__(self, configService: ConfigurationService):
		self.configurationService = configService
		self.device_sources = self.load_device_sources()

	def load_device_sources(self):
		device_sources = self.configurationService.config["deviceSources"]
		loaded_sources = []
		for source in device_sources:
			loaded_source = create_device_source(
				name = source["uuid"],
				uuid = source["name"],
				devices = source["devices"],
				protocol = source["protocol"]
			)
			loaded_sources.append(loaded_source)
			log.debug(f"""Loaded {source["protocol"]} source named: {source["name"]}""")
		return loaded_sources

	def run(self):
		log.info(f"GatewayService fully initalised, starting device collection for {len(self.device_sources)} device sources")
		while True:
			sleep(2.0)
			print("...")