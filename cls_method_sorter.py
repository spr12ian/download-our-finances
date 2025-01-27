from redbaron import RedBaron
import shutil
from pathlib import Path


class MethodSorter:
    def __init__(self, file_path, class_name):
        self.file_path = Path(file_path)
        self.class_name = class_name

        # Validate file path
        if not self.file_path.is_file():
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def sort_methods_in_class(self):
        """Sorts top-level methods in the specified class alphabetically."""
        # Read the source file
        try:
            with self.file_path.open("r") as source:
                code = source.read()
                red = RedBaron(code)
        except Exception as e:
            raise RuntimeError(f"Failed to parse the file: {e}")

        # Locate the target class
        class_node = next(
            (
                node
                for node in red.find_all("ClassNode")
                if node.name == self.class_name
            ),
            None,
        )

        if not class_node:
            raise ValueError(f"Class '{self.class_name}' not found in {self.file_path}")

        # Collect and sort top-level methods
        methods = [node for node in class_node.body if node.type == "def"]
        sorted_methods = sorted(methods, key=lambda x: x.name)

        # Replace the existing methods with sorted ones, preserving other class body items
        class_node.body = [
            node for node in class_node.body if node.type != "def"
        ] + sorted_methods

        # Write the modified code back to the file
        backup_path = self.file_path.with_suffix(".bak")
        try:
            shutil.copy(self.file_path, backup_path)  # Create a backup
            with self.file_path.open("w") as source:
                source.write(red.dumps())
            print(f"Methods in class '{self.class_name}' sorted successfully.")
            print(f"A backup of the original file has been saved as: {backup_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to write the sorted class to the file: {e}")


# Example usage:
# sorter = MethodSorter("example.py", "MyClass")
# sorter.sort_methods_in_class()
