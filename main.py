from osgate.cli import parse_args
from osgate.gateway import GatewayService
from osgate.configuration import ConfigurationService, ConfigurationArguments


def main():
    args = ConfigurationArguments(parse_args())
    configService = ConfigurationService(args)
    gatewayService = GatewayService(configService)
    gatewayService.run()


if __name__ == "__main__":
    main()
