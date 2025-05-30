import os
import yaml


class ConfigError(Exception):
    pass


class ConfigHelper:
    CONFIG_FILE_NAME = "config.yml"

    def __init__(self, config_path=None) -> None:
        self.path = config_path or self.CONFIG_FILE_NAME
        if not os.path.exists(self.path):
            raise ConfigError(f"Config file '{self.path}' not found.")
        with open(self.path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, key_path, default=None):
        keys = key_path.split(".")
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        # Support env override: ENV_<key_path> with underscores
        env_key = "ENV_" + "_".join(keys).upper()
        return os.getenv(env_key, value)



