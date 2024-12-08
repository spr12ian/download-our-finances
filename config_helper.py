import configparser

class ConfigHelper:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def __getitem__(self, key):
        return self.config[key]
