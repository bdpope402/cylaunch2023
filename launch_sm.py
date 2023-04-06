import rocketcheck
import execute_instruction
import time
import os
from cyllogger import cyllogger 
import hat_test

WAIT_TIME = 1800 #30 minute sleep time
IN_FLIGHT_TIME = 180 # 3 minute flight

FLAGS_FOLDER = "/home/cylaunch/payload_code/flags/"
STATE_FLAGS_DIR = FLAGS_FOLDER + "launchFlags/"

#Absolute Path to user customizable Flags
SKIP_SLEEP_PATH = FLAGS_FOLDER + "skipSleep.cyl"
SKIP_SM_PATH = FLAGS_FOLDER + "SkipSM.cyl"

#Flags to allow the raspberry pi to stay on between states. Will look for the State_S and State _F flags
SETUP_F = STATE_FLAGS_DIR + "setupF.cyl"
AWAITING_LAUNCH_F = STATE_FLAGS_DIR + "awaitingLaunchF.cyl"
IN_FLIGHT_F = STATE_FLAGS_DIR + "inFlightF.cyl"
CONFIRM_LANDING_F = STATE_FLAGS_DIR + "confirmLandingF.cyl"
AWAIT_MESSAGE_F = STATE_FLAGS_DIR + "awaitMessageF.cyl"
EXECUTE_INSTRUCTION_F = STATE_FLAGS_DIR + "executeInstructionF.cyl"

instruction_string = ""


log = cyllogger("sm_log")

def main():
    if(os.path.exists(SETUP_F) == False):
        setup_state()
    if(os.path.exists(AWAITING_LAUNCH_F) == False):
        awaiting_launch_state()
    if(os.path.exists(IN_FLIGHT_F) == False):
        in_flight_state()
    if(os.path.exists(CONFIRM_LANDING_F) == False):
        confirm_landing_state()
    if(os.path.exists(AWAIT_MESSAGE_F) == False):
        await_message_state()

    #find upright door, launch fm_rtl and multimon


def setup_state():
    log.writeTo("Entered " + __name__)
    if(os.path.exists(SKIP_SLEEP_PATH) == False):
        log.writeTo(f"Entering setup sleep, sleeping for: {str(WAIT_TIME/60)} minutes.")
        time.sleep(WAIT_TIME)
        log.writeTo("Exiting setup sleep.")
    else:
        log.writeTo("skipSleep.cyl exists, immediately checking accelerometer data")
    create_file(SETUP_F)
    log.writeTo("Exited " + __name__)

def awaiting_launch_state():
    log.writeTo("Entered " + __name__)
    while(rocketcheck.checkIfLaunching() == False):
        time.sleep(1)
    create_file(AWAITING_LAUNCH_F)
    log.writeTo("Exited " + __name__)

def in_flight_state():
    log.writeTo("Entered " + __name__)
    time.sleep(IN_FLIGHT_TIME)
    create_file(IN_FLIGHT_F)
    log.writeTo("Exited " + __name__)

def confirm_landing_state():
    log.writeTo("Entered " + __name__)
    while(rocketcheck.checkIfLanded() == False):
        time.sleep(1)
    create_file(CONFIRM_LANDING_F)
    log.writeTo("Exited " + __name__)

def await_message_state():
    global instruction_string
    log.writeTo("Entered " + __name__)
    #TODO implement radio functions
    create_file(AWAIT_MESSAGE_F)
    log.writeTo("Exited " + __name__)

def execute_instruction_state():
    global instruction_string
    log.writeTo("Entered " + __name__)
    os.system("python3 execute_instruction. py " + instruction_string)
    create_file(EXECUTE_INSTRUCTION_F)
    log.writeTo("Exited " + __name__)


def create_file(path):
    os.system("touch " + path)

if __name__ == "__main__":
        main()