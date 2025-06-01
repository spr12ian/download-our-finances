from our_finances.classes.config import Config
from our_finances.classes.os_helper import OsHelper


class FileHelper:
    def __init__(self, file_path: str = ""):
        self.file_path = file_path

    def clear(self):
        file_path = self.file_path
        with open(file_path, "w"):
            pass

    def print(self, message: str = ""):
        file_path = self.file_path
        with open(file_path, "a") as file:
            file.write(message + "\n")

    def set_output_from_file(self, file_path: str) -> None:
        self.file_path = self.get_output_path(file_path)
        self.clear()

    def get_output_path(self, file_path: str, output_directory: str = "") -> str:
        """
        Get the output path for a file based on the output directory.
        """
        osh = OsHelper()
        stem = osh.get_stem(file_path)

        if output_directory == "":
            config = Config()
            output_directory = config.get("OUTPUT_DIRECTORY")

        output_path = "/".join([output_directory, stem + ".txt"])
        return output_path
