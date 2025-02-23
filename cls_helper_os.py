from cls_helper_config import ConfigHelper
import os


class OsHelper:
    def get_basename(self, path):
        return os.path.basename(path)
    
    def get_extension(self, path):
        return os.path.splitext(os.path.basename(path))[1]
    
    def get_home_directory(self):
        return os.path.expanduser("~")
    
    def get_stem(self, path):
        return os.path.splitext(os.path.basename(path))[0]
