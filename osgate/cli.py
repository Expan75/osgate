from argparse import ArgumentParser

def parse_args():
	parser = ArgumentParser(description='Argument parser')
	parser.add_argument('--config', "-c", dest="config", type=str, help='Absolute Configuration filepath')
	parser.add_argument('--debug', "-d", dest="debug", action='store_true', help='Activate debug log')
	return parser.parse_args()