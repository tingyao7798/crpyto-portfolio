""" module where the commonly used methods are """
# core modules
import os
import logging.config
import yaml

# third party modules


def setup_logging(default_path='settings/logging.yaml',
                  default_level=logging.INFO):
    """Setup logging configuration
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as file:
            config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

