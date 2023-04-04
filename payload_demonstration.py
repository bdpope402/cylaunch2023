from cyllogger import cyllogger
import os
import RPi.GPIO as GPIO
import sys
import signal
import UpAngle
from move import move
import time

GPIO.setwarnings(False)
BUTTON_GPIO = 20
TEST_INSTRUCTION = "CALLSIGN A1 B2 D4 C3 E5 C3 F6 C3"
log = cyllogger("payload_demo")
zero = False

global move_local
local_move = move()
def main():
    global move_local
    global zero
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(
        BUTTON_GPIO, GPIO.BOTH, callback=button_callback, bouncetime=50
    )
    
    #local_move = move()
    correct_door = False
    while(not correct_door):
        local_move.spinF(360)
        # while(not zero):
        #     local_move.spinF(5)
        #     time.sleep(0.5)
        #     print(f"Zero is: {zero}")
        zero_angle = UpAngle.AngleToUp()
        move_angle = 0
        print(f"zero_angle is: {zero_angle}")

        if(zero_angle <= 45):
            print("Do nothing")
        elif(zero_angle <= 135):
            move_angle = 90
        elif(zero_angle <= 225):
            move_angle = 180
        elif(zero_angle <= 315):
            move_angle = 270

        local_move.spinB(move_angle) #move
        test_angle = UpAngle.AngleToUp()
        if(test_angle >= 315 or test_angle <= 45):
            correct_door = True
    
    print("Door Found!!!!")


    # signal.signal(signal.SIGINT, signal_handler)
    # signal.pause()

    # Call the code to execute the instructions
    # os.system("python3 /home/cylaunch/payload_code/execute_instruction.py " + TEST_INSTRUCTION)


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


# This needs to be updated to reset the angle to 0 everytime
def button_callback(channel):
    global zero
    if not GPIO.input(BUTTON_GPIO):
        log.writeTo("Button pressed!")
        print("Button pressed!")
        zero = True
    else:
        print("Button Released")
        log.writeTo("Button released!")


def moveToUp():
    global local_move
    rAng = UpAngle.AngleToUp()
    log.writeTo(f"Roll: {rAng}")
    turn = int(rAng / 3.8)
    log.writeTo(f"Turn: {turn}")
    local_move.spinF(turn)


if __name__ == "__main__":
    main()
