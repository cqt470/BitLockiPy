from colorama import Fore
import os

class File:
    def __init__(self, path=None):
        if not path:
            print(Fore.YELLOW + f"Warning: Please provide a valid path.")
        
        self.path = path

    def check_exists(self):
        return os.path.exists(self.path)
    
    def create(self):
        open(self.path, "w").close()

    def append(self, content):
        with open(self.path, "a") as f:
            f.write(f"{content}\n")
            f.close()

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def read_binary(self):
        with open(self.path, "rb") as f:
            return f.read()