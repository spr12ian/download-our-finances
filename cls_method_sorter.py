import ast
import shutil
from pathlib import Path


class MethodSorter(ast.NodeVisitor):
    def __init__(self, file_path, class_name):
        self.file_path = Path(file_path)
        self.class_name = class_name
        self.methods = []

        # Validate file path
        if not self.file_path.is_file():
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def visit_ClassDef(self, node):
        """Collect top-level methods in the specified class."""
        if node.name == self.class_name:
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    self.methods.append(item)
        # No need to call generic_visit here to avoid traversing nested classes
        # or further levels within the class.

    def sort_methods_in_class(self):
        """Sorts top-level methods in the specified class alphabetically."""
        # Read the source file
        try:
            with self.file_path.open("r") as source:
                tree = ast.parse(source.read())
        except Exception as e:
            raise RuntimeError(f"Failed to parse the file: {e}")

        # Locate the target class
        class_node = next(
            (
                node
                for node in tree.body
                if isinstance(node, ast.ClassDef) and node.name == self.class_name
            ),
            None,
        )

        if not class_node:
            raise ValueError(f"Class '{self.class_name}' not found in {self.file_path}")

        # Collect top-level methods
        self.methods = []
        self.visit(class_node)

        if not self.methods:
            print(f"No methods found in class '{self.class_name}'. No changes made.")
            return

        # Sort methods alphabetically by name
        sorted_methods = sorted(self.methods, key=lambda x: x.name)

        # Replace the existing methods with sorted ones, preserving other class body items
        class_node.body = [
            node
            for node in class_node.body
            if not isinstance(node, ast.FunctionDef)
        ] + sorted_methods

        # Write the modified tree back to the file
        backup_path = self.file_path.with_suffix(".bak")
        try:
            shutil.copy(self.file_path, backup_path)  # Create a backup
            with self.file_path.open("w") as source:
                source.write(ast.unparse(tree))
            print(f"Methods in class '{self.class_name}' sorted successfully.")
            print(f"A backup of the original file has been saved as: {backup_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to write the sorted class to the file: {e}")


# Example usage:
# sorter = MethodSorter("example.py", "MyClass")
# sorter.sort_methods_in_class()
