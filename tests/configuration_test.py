import os
import sys
import unittest
from pprint import pprint
from osgate import configuration

from osgate.connectors.factory import create_connector

class configurationServiceTests(unittest.TestCase):

    def test_invalid_config_dir(self):
        args = configuration.ConfigurationArguments(True, "/")
        with self.assertRaises(IsADirectoryError):
            configurationService = configuration.ConfigurationService(args)    

    def test_invalid_config_path(self):
        args = configuration.ConfigurationArguments(True, "/something.txt")
        with self.assertRaises(FileNotFoundError):
            configurationService = configuration.ConfigurationService(args)

    def test_valid_config(self):
        args = configuration.ConfigurationArguments(True, "osgate.json")
        configurationService = configuration.ConfigurationService(args)
        self.assertEqual(configurationService.filepath == args.filepath)


class connectorFactoryTests(unittest.TestCase):

    def test_invalid_data(self):
        with self.assertRaises(Exception):
            create_connector({ "data": [1,2,3] })