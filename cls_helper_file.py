from cls_helper_config import ConfigHelper
from cls_helper_log import LogHelper
from cls_helper_os import OsHelper


class FileHelper:
    def __init__(self, file_path):
        self.l = LogHelper("FileHelper")
        # self.l.set_level_debug()

        self.file_path = file_path

        config = ConfigHelper()

        self.output_directory = config["Output"]["directory"]

    def clear(self):
        file_path = self.file_path
        with open(file_path, "w") as file:
            pass

    def print(self, message):
        file_path = self.file_path
        with open(file_path, "a") as file:
            print(
                message,
                file=file,
            )
