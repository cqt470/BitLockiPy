import os

class Configs:
    def __init__(self):
        self.__base_path = os.path.realpath(f"{__file__}/../")
        
        # I path sono relativi a ~/src/
        self.paths = {
            "log_dir": f"{self.__base_path}\\logs\\",
            "log_file": f"{self.__base_path}\\logs\\.log",
        }