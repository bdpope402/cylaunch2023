#----------------------------------------------------
# Executes the payload instruction string according 
# to section 4.2.2
#----------------------------------------------------
import sys
import os
from misc_tests.servoTurn import servoTurn
from cyllogger import cyllogger
from datetime import datetime
from photo_editor import photo_editor

# Declare globals and constants
NASA_CALLSIGN = "KQ4CTL-4"
global servo1_angle
global servo2_angle
servo1_angle = 0
servo2_angle = 140

# Create global moveServo object
global moveServo
moveServo = servoTurn()




def main():
    # Create global variables to track what filters should be applied as per commands
    global greyscale
    global rotate_180
    global custom_filter
    global moveServo

    # Initialize globals
    greyscale = False
    rotate_180 = False
    custom_filter = False

    # Create Logger object
    log = cyllogger("ex_instruction_log")

    # Center Servo
    moveServo.moveServo(servo2_angle)

    # Verify NASA callsign
    num_args = len(sys.argv)
    if(verifyCallSign(sys.argv[0]) == False):
        log.writeTo("WARNING: " + sys.argv[0] + "DOES NOT MATCH EXPECTED CALL SIGN OF " + NASA_CALLSIGN)
        print("WARNING: " + sys.argv[0] + "DOES NOT MATCH EXPECTED CALL SIGN OF " + NASA_CALLSIGN)

    # Iterate through the command string and execute them
    i = 1 #start at 1, the first argument is the command
    while(i < num_args):
        command = str(sys.argv[i]).upper()
        ex_command(log, command)
        log.writeTo(command)
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

    #----------------------------------------------------
    # A1: Turn camera 60º to the right
    #----------------------------------------------------
    if(command == "A1"):
        log.writeTo("Entering A1: Turning Camera 60 Right")
        if(servo2_angle + 60 < 0):
            log.writeTo("Negative! Going to 260")
            servo2_angle = 260
        elif(servo2_angle + 60 > 260):
            log.writeTo("Over 260! Going to 20")
            servo2_angle = 20
        else:
            servo2_angle += 60
        
        success = moveServo.moveServo(servo2_angle)
        log.writeTo("Exiting A1")

    #----------------------------------------------------
    # B2: Turn camera 60º to the left
    #----------------------------------------------------
    elif(command == "B2"):
        log.writeTo("Entering B2: Turning camera -60")
        if(servo2_angle - 60 < 0):
            log.writeTo("Negative! Going to 260")
            servo2_angle = 260
        elif(servo2_angle - 60 > 260):
            log.writeTo("Over 260! Going to 20")
            servo2_angle = 20
        else:
            servo2_angle -= 60
        success = moveServo.moveServo(servo2_angle)
        log.writeTo("Exiting B2")
    #----------------------------------------------------
    # C3: Take picture and apply filters
    #----------------------------------------------------
    elif(command == "C3"):
        log.writeTo("Entering C3: Taking Picture")
        photo_path = "/home/cylaunch/payload_code/photos/" + current_time + ".jpg"

        # Command OS to take a photo
        os.system("raspistill -o " + photo_path)
        editor.changeImage(photo_path)

        # Apply appliciable filters
        if(greyscale == True):
            log.writeTo("Applying greyscale filter.")
            editor.greyscale()
        if(rotate_180 == True):
            editor.flip_180()
            log.writeTo("Applying 180 degree rotation.")
        if(custom_filter == True):
            editor.custom_filter()
            log.writeTo("Applying custom filter.")

        # Apply timestamp as per 4.2.1.3
        editor.timestamp()

        #apply changes
        editor.write()
        success = 1
        log.writeTo("Exiting C3. Photo available at: " + photo_path)

    #----------------------------------------------------
    # D4: Change camera mode from color to grayscale
    #----------------------------------------------------
    elif(command == "D4"):
        log.writeTo("Entering D4: Changing to greyscale")
        greyscale = True
        if(greyscale == True):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting D4")

    #----------------------------------------------------
    # E5: Change camera mode back from grayscale to color
    #----------------------------------------------------
    elif(command == "E5"):
        log.writeTo("Entering E5: Changing to color")
        greyscale = False
        if(greyscale == False):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting E5")

    #----------------------------------------------------
    # F6: Rotate image 180º
    #----------------------------------------------------
    elif(command == "F6"):
        log.writeTo("Entering F6: Rotate images 180 deg")
        rotate_180 = True
        if(rotate_180 == True):
            success = 1
        else:
            success = -1
        log.writeTo("Exiting F6")

    #----------------------------------------------------
    # G7: Special effects filter
    #----------------------------------------------------
    elif(command == "G7"):
        log.writeTo("Entering G7: APPLYING custom filter")
        custom_filter = True
        if(custom_filter == True):
            success = 1
        else:
            success = -1
        log.writeTo("exiting G7")

    #----------------------------------------------------
    # H8: Clear all filters
    #----------------------------------------------------
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
        print("") # Empty else. Should do nothing

    # Write success / failure to log
    if(success < 0):
        log.writeTo("Returned error while executing " + command)
    else:
        log.writeTo(str("successfully executed " + command))

if __name__ == "__main__":
    main()
