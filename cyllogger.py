from datetime import datetime
from datetime import time

class cyllogger:
    def __init__(self, name):
        self.logfile = open("logs/" + name + str(datetime.now()) + ".txt", "w")
    
    def writeTo(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.logfile.write("[" + str(current_time) + "] " + message + "\n")
    
    def cleanup(self):
        self.logfile.close()