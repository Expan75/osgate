import pytest
from osgate import configuration

def test_invalid_config_directory():
    args = configuration.configurationigurationArguments(True, "/")
    with pytest.raises(IsADirectoryError):
        configurationigService = configuration.configurationigurationService(args)

def test_invalid_configurationig_filepath():
    args = configuration.configurationigurationArguments(True, "/something.txt")
    with pytest.raises(FileNotFoundError):
        configurationigService = configuration.configurationigurationService(args)

def test_valid_configurationig_filepath():
    args = configuration.configurationigurationArguments(True, "osgate.json")
    configurationigService = configuration.configurationigurationService(args)
    assert configurationigService.filepath == args.filepath

def test_configuration_read():
    assert True

def test_partial_configuration_write():
    assert True

def test_complete_configuration_write():
    assert True
