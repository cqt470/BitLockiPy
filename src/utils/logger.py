from datetime import datetime
from colorama import Fore, Back, Style
from configs import Configs
from utils.file import File

class Logger:
    def __init__(self):
        self.__severity_configs = {
            "types": [
                "DEBUG", "INFO", "NOTICE", "WARNING", "ERROR",
                "CRITICAL", "ALERT", "EMERGENCY"
            ],
            "colors": {
                "DEBUG": Fore.CYAN,
                "INFO": Fore.GREEN,
                "NOTICE": Fore.BLUE,
                "WARNING": Fore.YELLOW,
                "ERROR": Fore.RED,
                "CRITICAL": Fore.RED,
                "ALERT": Fore.MAGENTA,
                "EMERGENCY": Fore.WHITE
            },
            "styles": {
                "DEBUG": Style.DIM,
                "NOTICE": Style.BRIGHT,
                "WARNING": Style.BRIGHT,
                "CRITICAL": Style.BRIGHT,
                "ALERT": Style.BRIGHT,
                "EMERGENCY": Style.BRIGHT
            },
            "backgrounds": {
                "ALERT": Back.MAGENTA,
                "EMERGENCY": Back.RED
            }
        }
        self.__configs = Configs()
        self.log_path = self.__configs.paths["log_file"]
        self.log_file = File(self.log_path)
        self.__create_log_file()

    def __create_log_file(self):
        if not self.log_file.check_exists():
            self.log_file.create()
            self.log(f"File di log creato in {self.log_path}")

    def __get_text(self, message, severity, formatted=True):
        severity = str(severity).upper()
        now = datetime.now().strftime("%d-%m-%Y::%H.%M.%S")

        color = self.__severity_configs["colors"].get(severity, Fore.WHITE)
        style = self.__severity_configs["styles"].get(severity, Style.NORMAL)
        back = self.__severity_configs["backgrounds"].get(severity, Back.RESET)

        prefix = f"[{now}] [{severity}]"

        if not formatted: return f"{prefix} {message}"

        return f"{style}{back}{color}{prefix} {message}{Style.RESET_ALL}"

    def __print_log(self, message, severity="DEBUG"):
        text = self.__get_text(message, severity)
        print(text)

    def __log_in_file(self, message, severity="DEBUG"):
        text = self.__get_text(message, severity, False)
        self.log_file.append(text)

    def log(self, message, severity="DEBUG"):
        self.__print_log(message, severity)
        self.__log_in_file(message, severity)

    def test_colors(self):
        for severity in self.__severity_configs["types"]:
            self.log("This is a test message", severity)