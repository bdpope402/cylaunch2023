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
    success = servoTurn.moveServo(2,servo2_angle)
    
def log(logfile, text):
    logfile.write(text + "\n")

def ex_command(logfile, command):
    global servo2_angle
    success = -1
    if(command == "A1"):
        servo2_angle += 60
        success = servoTurn.moveServo(2,servo2_angle)
    elif(command == "B2"):
        servo2_angle -= 60
        success = servoTurn.moveServo(2, servo2_angle)
    elif(command == "C3"):
        print("got c3")
    else:
        print("")
    if(success < 0):
        log(logfile, "Returned error while executing " + command)
    else:
        log(logfile, str("successfully executed " + command))
def turn_servo(degrees, right):
    print("AHHHHHHH")
if __name__ == "__main__":
    main()
