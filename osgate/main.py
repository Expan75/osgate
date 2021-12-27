import json
import logging
from time import sleep
from argparse import ArgumentParser

class Device():
	def __init__(self, name: str, uuid: str, protocol: str):
		self.name = name
		self.uuid = uuid
		self.protocol = protocol

	def ping():
		pass

class Driver():
	def __init__(self, filepath: str, debug=False):
		self.logger = self.load_logger(debug)
		self.config = self.load_configuration(filepath)
		self.devices = self.load_devices()

	def load_logger(self, debug: bool):
		log_level = logging.DEBUG if debug else logging.INFO
		logging.basicConfig(level=log_level)
		return logging.getLogger(__name__)

	def load_configuration(self, filepath: str) -> dict:
		try: 
			with open(filepath) as file:
				return json.load(file)
		except FileNotFoundError:
			self.logger.warning(f"Configuration file not found at {filepath}, exiting...")
			exit()

	def load_devices(self):
		return [Device(device["name"], device["uuid"], device["protocol"]) for device in self.config["devices"]]

	def run(self):
		self.logger.debug("driver fully initalised")
		print("fetching data for following devices: ")
		for device in self.devices:
			print(device.name)
		while True:
			sleep(2.0)
			print("...")

if __name__ == "__main__":
	parser = ArgumentParser(description='Argument parser')
	parser.add_argument('--config', "-c", type=str, help='Absolute Configuration filepath')
	parser.add_argument('--debug', "-d", dest="debug", action='store_true', help='Activate debug log')
	args = parser.parse_args()
	driver = Driver(args.config, args.debug)
	driver.run()
