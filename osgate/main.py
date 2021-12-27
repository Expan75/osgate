from argparse import ArgumentParser
from configuration import load_configuration
from time import sleep

class Driver():
	def __init__(self, configuration_path: str):
		self.configuration = load_configuration(configuration_path)

	def run():
		print("driver fully initalised")
		while True:
			print("hello world!")
			sleep(0.5)

if __name__ == "__main__":
	parser = ArgumentParser(description='Argument parser')
	parser.add_argument('--config', type=str, help='Absolute Configuration filepath')
	args = parser.parse_args()
	driver = Driver(args.config).run()
