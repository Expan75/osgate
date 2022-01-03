from cli import cli
from gateway import GatewayService
from configuration import ConfigurationService, ConfigurationArguments

def main():
	args = ConfigurationArguments(cli())
	configService = ConfigurationService(args)
	gatewayService = GatewayService(configService)
	gatewayService.run()

if __name__ == "__main__":
	main()