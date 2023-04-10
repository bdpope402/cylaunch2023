import sys
import os
from servoTurn import servoTurn
from cyllogger import cyllogger
from datetime import datetime
from photo_editor import photo_editor

NASA_CALLSIGN = "KQ4CTL-4"

global servo1_angle
global servo2_angle
servo1_angle = 0
servo2_angle = 140
global moveServo
moveServo = servoTurn()




def main():
    global greyscale
    global rotate_180
    global custom_filter
    global moveServo
    greyscale = False
    rotate_180 = False
    custom_filter = False
    log = cyllogger("ex_instruction_log")
    moveServo.moveServo(servo2_angle)
    num_args = len(sys.argv)
    if(verifyCallSign(sys.argv[0]) == False):
        log.writeTo("WARNING: " + sys.argv[0] + "DOES NOT MATCH EXPECTED CALL SIGN OF " + NASA_CALLSIGN)
        print("WARNING: " + sys.argv[0] + "DOES NOT MATCH EXPECTED CALL SIGN OF " + NASA_CALLSIGN)
    i = 1 #start at 1, the first argument is the command
    # logfile = open("logs/landinglog" + str(datetime.now()) + ".txt", "w")
    while(i < num_args):
        command = str(sys.argv[i]).upper()
        ex_command(log, command)
        #log.writeTo(command)
        i += 1

def verifyCallSign(callsign):
    return (NASA_CALLSIGN ==  callsign)
    

def ex_command(log, command):
    global moveServo
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    editor = photo_editor("/home/cylaunch/payload_code/DO_NOT_DELETE/daniel.jpg")
    global greyscale
    global rotate_180
    global custom_filter
    global servo2_angle
    success = -1
    if(command == "A1"):
        log.writeTo("Entering A1: Turning Camera 60 RIght")
        if(servo2_angle + 60 < 0):
            log.writeTo("Negative! Going to 260")
            servo2_angle = 260
        elif(servo2_angle + 60 > 220):
            log.writeTo("Over 260! Going to 20")
            servo2_angle = 20
        else:
            servo2_angle += 60
        
        success = moveServo.moveServo(servo2_angle)
        log.writeTo("Exiting A1")
    elif(command == "B2"):
        log.writeTo("Entering B2: Turning camera -60")
        if(servo2_angle - 60 < 0):
            log.writeTo("Negative! Going to 260")
            servo2_angle = 260
        elif(servo2_angle - 60 > 220):
            log.writeTo("Over 260! Going to 20")
            servo2_angle = 20
        else:
            servo2_angle += 60
        servo2_angle -= 60
        success = moveServo.moveServo(servo2_angle)
        log.writeTo("Exiting B2")
    elif(command == "C3"):
        log.writeTo("Entering C3: Taking Picture")
        photo_path = "/home/cylaunch/payload_code/photos/" + current_time + ".jpg"
        os.system("raspistill -o " + photo_path)
        editor.changeImage(photo_path)
        if(greyscale == True):
            log.writeTo("Applying greyscale filter.")
            editor.greyscale()
            
        if(rotate_180 == True):
            editor.flip_180()
            log.writeTo("Applying 180 degree rotation.")
        if(custom_filter == True):
            editor.custom_filter()
            log.writeTo("Applying custom filter.")
        editor.timestamp()
        editor.write()
        success = 1
        log.writeTo("Exiting C3. Photo available at: " + photo_path)
    elif(command == "D4"):
        log.writeTo("Entering D4: Changing to greyscale")
        greyscale = True
        if(greyscale == True):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting D4")
    elif(command == "E5"):
        log.writeTo("Entering E5: Changing to color")
        greyscale = False
        if(greyscale == False):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting E5")
    elif(command == "F6"):
        log.writeTo("Entering F6: Rotate images 180 deg")
        rotate_180 = True
        if(rotate_180 == True):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting F6")
    elif(command == "G7"):
        log.writeTo("Entering G7: APPLYING custom filter")
        custom_filter = True
        if(custom_filter == True):
            success = 1
        else:
            success = -1
        log.writeTo("exiting G7")
    elif(command == "H8"):
        log.writeTo("Entering H8: Clearing all filters")
        greyscale = False
        rotate_180 = False
        custom_filter = False
        if(greyscale == False and rotate_180 == False and custom_filter == False):
            success = 1
        else:
            success = -1
        log.writeTo("exiting H8")
    else:
        print("")
    if(success < 0):
        log.writeTo("Returned error while executing " + command)
    else:
        log.writeTo(str("successfully executed " + command))

if __name__ == "__main__":
    main()
