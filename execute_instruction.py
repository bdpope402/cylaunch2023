import sys
import os
import servoTurn
from datetime import datetime

global servo1_angle
global servo2_angle
servo1_angle = 0
servo2_angle = 0

def main():
    num_args = len(sys.argv)
    i = 1 #start at 1, the first argument is the command
    init()
    logfile = open("logs/landinglog" + str(datetime.now()) + ".txt", "w")
    while(i < num_args):
        command = str(sys.argv[i]).upper()
        ex_command(logfile, command)
        #log(logfile, command)
        i = i + 1
    logfile.close()

def init():
    servoTurn.moveServo(2,servo2_angle)
    
def log(logfile, text):
    logfile.write( text + "\n")

def ex_command(logfile, command):
    global servo2_angle
    success = -1
    if(command == "A1"):
        log(logfile, "Entering A1: Turning Camera 60")
        servo2_angle += 60
        success = servoTurn.moveServo(2,servo2_angle)
        log(logfile, "Exiting A1")
    elif(command == "B2"):
        log(logfile,"Entering B2: Turning camera -60")
        servo2_angle -= 60
        success = servoTurn.moveServo(2, servo2_angle)
        log(logfile,"Exiting B2")
    elif(command == "C3"):
        log(logfile,"Enginering C3: Taking Picture")
        log(logfile,"Exiting C3")
    elif(command == "D4"):
        log(logfile, "Entering D4: Changing to greyscale")
        log(logfile, "Exiting D4")
    elif(command == "E5"):
        log(logfile, "Entering E5: Changing to color")
        log(logfile, "Exiting E5")
    elif(command == "F6"):
        log(logfile, "Entering F6: Rotate images 180 deg")
        log(logfile, "Exiting F6")
    elif(command == "G7"):
        log(logfile, "Entering G7: Clearing all filters")
        log(logfile, "exiting G7")
    else:
        print("")
    if(success < 0):
        log(logfile, "Returned error while executing " + command)
    else:
        log(logfile, str("successfully executed " + command))

if __name__ == "__main__":
    main()
