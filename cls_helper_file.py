from cls_helper_config import ConfigHelper
from cls_helper_log import LogHelper
from cls_helper_os import OsHelper


class FileHelper:
    def __init__(self, file_path: str = ""):
        self.l = LogHelper("FileHelper")
        # self.l.set_level_debug()

        self.file_path = file_path

    def clear(self):
        file_path = self.file_path
        with open(file_path, "w") as file:
            pass

    def print(self, message):
        file_path = self.file_path
        with open(file_path, "a") as file:
            file.write(message + "\n")

    def set_output_from_file(self, file_path: str) -> None:
        self.file_path = self.get_output_path(file_path)
        self.l.debug(f"Output path set to: {self.file_path}")
        self.clear()
        return self.file_path

    def get_output_path(self, file_path: str, output_directory: str = "") -> str:
        """
        Get the output path for a file based on the output directory.
        """
        self.l.debug(f"file_path: {file_path}")
        osh = OsHelper()
        if output_directory == "":
            config = ConfigHelper()
            output_directory = config["Output"]["directory"]
            self.l.debug(f"output_directory: {output_directory}")
        stem = osh.get_stem(file_path)
        self.l.debug(f"stem: {stem}")
        output_path = "/".join([output_directory, stem + ".txt"])
        self.l.debug(f"output_path: {output_path}")
        return output_path
