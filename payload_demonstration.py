from move import move
from cyllogger import cyllogger
import os
import RPi.GPIO as GPIO
import sys
import signal

GPIO.setwarnings(False)
BUTTON_GPIO = 20
TEST_INSTRUCTION = "CALLSIGN A1 B2 D4 C3 E5 C3 F6 C3"

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=button_callback, bouncetime=50)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    #Call the code to execute the instructions 
    os.system("python3 /home/cylaunch/payload_code/execute_instruction.py " + TEST_INSTRUCTION)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

#This needs to be updated to 
def button_callback(channel):
    if not GPIO.input(BUTTON_GPIO):
        print("Button pressed!")
    else:
        print("Button released!")

if __name__ == "__main__":
    main()