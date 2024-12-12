import configparser


class ConfigHelper:
    def __init__(self):
        print(__class__)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def __getitem__(self, key):
        print(__class__.__name__)
        print(key)
        if key not in self.config:
            raise KeyError(f"Key '{key}' not found in config file")

        return self.config[key]
