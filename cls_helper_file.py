from cls_helper_config import ConfigHelper
from cls_helper_log import LogHelper
from cls_helper_os import OsHelper


class FileHelper:
    def __init__(self):
        self.l = LogHelper("FileHelper")
        # self.l.set_level_debug()

        config = ConfigHelper()

        self.output_directory = config["Output"]["directory"]
