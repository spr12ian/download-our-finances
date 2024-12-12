import configparser


class ConfigHelper:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def __getitem__(self, key):
        if key not in self.config:
            raise KeyError(f"Key '{key}' not found in config file")

        return self.config[key]
