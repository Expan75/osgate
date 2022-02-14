import pytest
from osgate import configuration

def test_invalid_config_directory():
    args = configuration.ConfigurationArguments(True, "/")
    with pytest.raises(IsADirectoryError):
        configurationService = configuration.ConfigurationService(args)


def test_invalid_configurationig_filepath():
    args = configuration.ConfigurationArguments(True, "/something.txt")
    with pytest.raises(FileNotFoundError):
        configurationService = configuration.ConfigurationService(args)


def test_valid_configurationig_filepath():
    args = configuration.ConfigurationArguments(True, "osgate.json")
    configurationService = configuration.ConfigurationService(args)
    assert configurationService.filepath == args.filepath


def test_configuration_read():
    assert True


def test_partial_configuration_write():
    assert True


def test_complete_configuration_write():
    assert True
