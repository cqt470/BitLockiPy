from utils.logger import Logger
from utils.file import File
from cryptography.fernet import Fernet

# https://www.geeksforgeeks.org/python/encrypt-and-decrypt-files-using-python/

class Encrypter:
    def __init__(self):
        self.logger = Logger()
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.key_directory = ""

    def encrypt_file(self, file_location):
        self.logger.log(f"Encrypting file: {file_location}")
        file = File(file_location)
        data = file.read_binary()
        encrypted_data = self.cipher.encrypt(data)
        new_file = File(f"{file_location}.enc")
        new_file.create()
        new_file.append(encrypted_data)
        new_file.append(self.key)
        self.logger.log(f"File encrypted successfully: {file_location}.enc")