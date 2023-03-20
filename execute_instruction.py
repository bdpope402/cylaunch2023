import sys
import os
from datetime import datetime

def main():
    num_args = len(sys.argv)
    i = 1 #start at 1, the first argument is the command
    init()
    logfile = open("logs/landinglog" + str(datetime.now()) + ".txt", "w")
    while(i < num_args):
        command = str(sys.argv[i]).upper()
        i = i + 1
    logfile.close()

def init():
    print(os.getcwd())
    

def log_cmd(command):
    logfile.write("Executed " + command + "\n")

def ex_command(command):
    if(command == "A1"):
        turn_servo(60, True)
        log(command)
    elif(command == "B2"):
        turn_servo(60, False)
    elif(command == "C3"):
        log(command)
    else:
        print("")

def turn_servo(degrees, right):
    print("AHHHHHHH")
if __name__ == "__main__":
    main()
