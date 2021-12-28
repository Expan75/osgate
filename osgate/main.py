import logging
from cli import cli
from conf import ConfigurationService
from gateway import GatewayService

def main():
	args = cli()

	log_level = logging.DEBUG if args.debug else logging.INFO
	logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	configService = ConfigurationService()
	gatewayService = GatewayService(configService)
	gatewayService.run()

if __name__ == "__main__":
	main()