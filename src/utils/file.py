from colorama import Fore
import os

class File:
    def __init__(self, path=None):
        if not path:
            print(Fore.YELLOW + f"Warning: Please provide a valid path.")
        
        self.path = path

        if not self.check_exists():
            print(Fore.YELLOW + f"Warning: The file '{self.path}' does not exist." + Fore.RESET)
            exit

    def check_exists(self):
        return os.path.exists(self.path)