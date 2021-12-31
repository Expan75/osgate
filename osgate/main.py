from cli import cli
from configuration import ConfigurationService, ConfigurationArguments
from gateway import GatewayService

def main():
	args = ConfigurationArguments(cli())
	configService = ConfigurationService(args)
	gatewayService = GatewayService(configService)
	gatewayService.run()

if __name__ == "__main__":
	main()