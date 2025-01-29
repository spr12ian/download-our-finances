from redbaron import RedBaron
import shutil
from pathlib import Path
from cls_helper_log import LogHelper


class MethodSorter:
    def __init__(self, file_path, class_name):
        self.l = LogHelper("MethodSorter")
        self.l.set_level_debug()
        self.l.debug(__file__)
        self.l.debug(f"file_path: {file_path}")
        self.l.debug(f"class_name: {class_name}")
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

        self.l.debug(f"Class '{self.class_name}' found in {self.file_path}")
        # Collect and sort top-level methods
        methods = [
            node for node in class_node.find_all("DefNode") if node.parent == class_node
        ]
        self.l.debug(f"{len(methods)} methods found in {self.class_name}")
        sorted_methods = sorted(methods, key=lambda x: x.name)


        # Preserve non-method elements (e.g., attributes, docstrings)
        class_body = [node for node in class_node.value if node.type != "def"]
        class_node.value = class_body + sorted_methods

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
