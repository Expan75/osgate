import os
import json
import logging
from dataclasses import dataclass
from typing import Optional

log = logging.getLogger(__name__)


@dataclass
class ConfigurationArguments:
    debug: bool
    filepath: Optional[str] = None


class ConfigurationService:
    """Handles all things configuration; mainly parsing and persisting a json config file (operates as singleton)"""

    def __init__(self, args: ConfigurationArguments):
        self.set_log_level(args.debug)
        self.filepath = (
            args.filepath
            if args.filepath is not None
            else os.path.join(os.getcwd(), "osgate.json")
        )
        self.parse_config()

    def set_log_level(self, debug: bool):
        log_level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    def parse_config(self, filepath):
        with open(filepath, "r") as config_file:
            parsed_config = json.load(config_file)
        self.config = parsed_config

    def flush_config(self, config: dict):
        with open(self.filepath, "w") as file:
            file.write(config)
