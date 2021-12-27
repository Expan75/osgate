import json

def load_configuration(configuration_filepath: str) -> dict:
    conf = json.loads(configuration_filepath)
    print(conf)