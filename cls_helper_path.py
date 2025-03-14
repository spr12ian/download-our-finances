from pathlib import Path


class PathHelper:
    def __init__(self, file_str: str) -> None:
        self.path = Path(file_str)

    def append_output_str(self, output_str: str) -> None:
        with self.path.open("a") as output:
            output.write(output_str)

    def write_output_str(self, output_str: str) -> None:
        with self.path.open("w") as output:
            output.write(output_str)
