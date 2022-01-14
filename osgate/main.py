from cli import parse_args
from gateway import GatewayService
from configuration import ConfigurationService, ConfigurationArguments

def main():
	args = ConfigurationArguments(parse_args())
	configService = ConfigurationService(args)
	gatewayService = GatewayService(configService)
	gatewayService.run()

if __name__ == "__main__":
	main()