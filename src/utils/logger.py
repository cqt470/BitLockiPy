from datetime import datetime
from colorama import Fore, Back, Style

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

    def log(self, message, severity="DEBUG"):
        severity = str(severity).upper()
        now = datetime.now().strftime("%d-%m-%Y::%H.%M.%S")

        color = self.__severity_configs["colors"].get(severity, Fore.WHITE)
        style = self.__severity_configs["styles"].get(severity, Style.NORMAL)
        back = self.__severity_configs["backgrounds"].get(severity, Back.RESET)

        prefix = f"[{now}] [{severity}]"
        text = f"{style}{back}{color}{prefix} {message}{Style.RESET_ALL}"

        print(text)

    def test_colors(self):
        for severity in self.__severity_configs["types"]:
            self.log("This is a test message", severity)