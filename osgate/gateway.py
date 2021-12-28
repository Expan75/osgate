import logging
from time import sleep
from conf import ConfigurationService
from devices import BaseDevice

log = logging.getLogger(__name__)

class GatewayService():
	def __init__(self, configService: ConfigurationService):
		self.configurationService = configService
		self.devices = self.load_devices()

	def load_devices(self):
		devices = self.configurationService.config["devices"]
		loaded_devices = []
		for device in devices:
			loaded_devices.append(BaseDevice(device["name"], device["uuid"]))
		return loaded_devices

	def run(self):
		log.info(f"GatewayService fully initalised, starting device collection for {len(self.devices)} devices")
		while True:
			sleep(2.0)
			print("...")