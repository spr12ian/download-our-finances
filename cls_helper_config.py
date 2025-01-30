import configparser
import os
import sys


class ConfigHelper:
    CONFIG_FILE_NAME="config.ini"

    def __getitem__(self, key):
        if key not in self.config:
            raise KeyError(f"Key '{key}' not found in config file")

        return self.config[key]
    def __init__(self):
        if os.path.exists(ConfigHelper.CONFIG_FILE_NAME):
            self.config = configparser.ConfigParser()
            self.config.read(ConfigHelper.CONFIG_FILE_NAME)
        else:
            print(f"Config file '{ConfigHelper.CONFIG_FILE_NAME}' not found.", file=sys.stderr)
            exit()
