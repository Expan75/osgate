import os
import json
import logging
from dataclasses import dataclass
from typing import Optional

log = logging.getLogger(__name__)

@dataclass
class ConfigurationArguments():
    debug: bool
    filepath: Optional[str] = None

class ConfigurationService():
    """Handles all things configuration; mainly parsing and persisting a json config file (operates as singleton)"""
    def __init__(self, args: ConfigurationArguments):
        self.set_log_level(args.debug)
        self.filepath = args.filepath if args.filepath is not None else os.path.join(os.getcwd(), "osgate.json")
        self.config = self.read_config_file()

    def set_log_level(self, debug: bool):
        log_level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def read_config_file(self):
        log.debug(f"trying to read config from: {self.filepath}")
        try:
            with open(self.filepath, "r") as config_file:
                config = json.load(config_file)
        except FileNotFoundError as e:
            log.critical(f"Configfile could not be found at {self.filepath}, resulting in FileNotFoundError: ", e)
            raise e
        log.debug("Loaded configuration file.")
        return config

    def flush_config_file(self, config: str):
        with open(self.filepath, "w") as file:
            file.write(config)