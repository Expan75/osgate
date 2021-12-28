import os
import json
import logging
from typing import Optional

log = logging.getLogger(__name__)

class ConfigurationService():
    def __init__(self, filepath: Optional[str]=None):
        self.filepath = filepath if filepath is not None else os.path.join(os.getcwd(), "osgate.json")
        log.debug(f"filepath set to: {self.filepath}")
        self.config = self.read_config_file()
    
    def read_config_file(self):
        log.debug(f"trying to read config from: {self.filepath}")
        try:
            with open(self.filepath, "r") as config_file:
                config = json.load(config_file)
        except FileNotFoundError as e:
            log.critical(f"Configfile could not be found at {self.filepath}, resulting in FileNotFoundError: ", e)
        return config

    def flush_config_file(self, config: str):
        with open(self.filepath, "w") as file:
            file.write(config)