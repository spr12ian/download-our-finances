import os

class OsHelper:
    def get_home_directory(self):
        return os.path.expanduser('~')
