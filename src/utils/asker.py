from utils.logger import Logger
from utils.file import File
from encrypt.encrypter import Encrypter

class Asker:
    def __init__(self):
        self.__steps = [
            {
                "label": "A file",
                "steps": [
                    {
                        "label": "The file's location",
                        "value": None
                    }
                ]
            }
        ]

        self.logger = Logger()
        self.encrypter = Encrypter()

    def __ask(self, options=None, question=None):
        if not question:
            self.logger.log("Insert a question!", "ERROR")
            return

        if not options:
            while True:
                answer = input(f"{question}\n> ")

                if answer:
                    return answer
                
                print("Please insert a valid answer\n")
            return

        while True:
            for index, key in enumerate(options):
                values = options[index]
                label = values["label"]

                print(f"[{index + 1}] - {label}")
            
            try:
                choice = int(input(f"{question}\n> "))

                if 0 < choice and choice <= len(options):
                    break
                
                print("Please insert a valid option\n")
            except ValueError:
                print("Please insert a valid option\n")

        self.logger.log(f"Registered choice. Q: {question}, A: {choice}")
        return choice

    def run(self):
        self.logger.log("Asker dialog started")
        print("Welcome in BitLockiPy, a file encryption tool by zerokelvin\n\nPlease choose what you want to encrypt from below.")
        
        # gestire il return
        self.__ask(self.__steps, "Choose what you want to encrypt")