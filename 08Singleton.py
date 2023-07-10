"""
Memory saving trick
Allows for a single instantiation of the object
"""

import time
import datetime

class Logger:

    class __Singleton:
        file_name = "fisier.txt"

        def __init__(self):
            print("Initialized")

        def log(self, log_msg):
            with open(self.file_name, "a") as f:
                f.write(f"{log_msg} - {datetime.datetime.now()}\n")

    __instance = None

    def __new__(cls):
        if not Logger.__instance:
            Logger.__instance = Logger.__Singleton()
            print("Made an instance")
        return Logger.__instance


logger = Logger()
logger.log("salutare")

time.sleep(2)

logger_d = Logger()
logger_d.log("Uraa!")