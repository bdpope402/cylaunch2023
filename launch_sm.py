import rocketcheck
import execute_instruction
import time
import os
from cyllogger import cyllogger 
import hat_test
import signal
from RadioDecoder import RadioDecoder
from subprocess import check_output
from move import move


#Set integers to do things
WAIT_TIME = 1800 #30 minute sleep time
IN_FLIGHT_TIME = 180 # 3 minute flight

#Folders to cut down on long strings
FLAGS_FOLDER = "/home/cylaunch/payload_code/flags/"
STATE_FLAGS_DIR = FLAGS_FOLDER + "launchFlags/"

#Absolute Path to user customizable Flags
SKIP_SLEEP_PATH = FLAGS_FOLDER + "skipSleep.cyl"
SKIP_SM_PATH = FLAGS_FOLDER + "SkipSM.cyl"
RADIO_OUTPUT_PATH = "/home/cylaunch/payload_code/radio_output/empty.txt"

#Flags to allow the raspberry pi to stay on between states. Will look for the State_S and State _F flags
SETUP_F = STATE_FLAGS_DIR + "setupF.cyl"
AWAITING_LAUNCH_F = STATE_FLAGS_DIR + "awaitingLaunchF.cyl"
IN_FLIGHT_F = STATE_FLAGS_DIR + "inFlightF.cyl"
CONFIRM_LANDING_F = STATE_FLAGS_DIR + "confirmLandingF.cyl"
AWAIT_MESSAGE_F = STATE_FLAGS_DIR + "awaitMessageF.cyl"
IN_POSITION_F = STATE_FLAGS_DIR + "inPos.cyl"
EXECUTE_INSTRUCTION_F = STATE_FLAGS_DIR + "executeInstructionF.cyl"
SM_COMPLETION_F = STATE_FLAGS_DIR + "smComplete.cyl"

#DEBUGGING STATEMENTS. Uncomment up to the state you want to run
os.system("touch " + SETUP_F)
os.system("touch " + AWAITING_LAUNCH_F)
os.system("touch " + IN_FLIGHT_F)
os.system("touch " + CONFIRM_LANDING_F)
os.system("touch " + AWAIT_MESSAGE_F)
# os.system("touch " + EXECUTE_INSTRUCTION_F)
# os.system("touch " + SM_COMPLETION_F)


#Variables
instruction_string = "A1 B2 C3"
NASA_CALLSIGN = "KQ4CTL-4"


log = cyllogger("sm_log")
local_move = move()
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
    if(os.path.exists(EXECUTE_INSTRUCTION_F) == False):
        execute_instruction_state()
    if(os.path.exists(SM_COMPLETION_F) == True):
        completed_cleanup_state()
        # Graceful shutdown
        os.system("sudo poweroff")


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
        time.sleep(0.5)
    #Lock Payload
    move.spinF(0.1)
    create_file(AWAITING_LAUNCH_F)
    log.writeTo("Exited " + __name__)

def in_flight_state():
    log.writeTo("Entered " + __name__)
    time.sleep(IN_FLIGHT_TIME)
    create_file(IN_FLIGHT_F)
    log.writeTo("Exited " + __name__)

def confirm_landing_state():
    log.writeTo("Entered " + __name__)
    move.releaseStepper()
    while(rocketcheck.checkIfLanded() == False):
        time.sleep(1)
    create_file(CONFIRM_LANDING_F)
    log.writeTo("Exited " + __name__)

def await_message_state():
    global instruction_string
    valid_message = False
    log.writeTo("Entered " + __name__)
    
    while(valid_message == False):
        #Start Radio
        os.system("/home/cylaunch/payload_code/radio.sh")
        #Waiting for file to be written to
        while(os.path.getsize(RADIO_OUTPUT_PATH) == 0):
            time.sleep(1)
        log.writeTo("Exited ""File Exists"" loop")
        #Create decoder once we have output
        decoder = RadioDecoder(RADIO_OUTPUT_PATH)
        decoder.decode64()
        pids = get_pid("radio.sh")
        if(decoder.callsign == NASA_CALLSIGN):
            instruction_string = decoder.FinalString
            valid_message = True
        else:
            valid_message = False
            #Delete file to start with a new output
            os.system("rm " + RADIO_OUTPUT_PATH)

        #Kill radio processes to either end them or restart them            
        for x in pids:
            os.kill(x, signal.SIGSTOP)

    create_file(AWAIT_MESSAGE_F)
    log.writeTo("Exited " + __name__)

def execute_instruction_state():
    global instruction_string
    log.writeTo("Entered " + __name__)
    #Pick door and extend
    os.system("python3 /home/cylaunch/payload_code/payload_demonstration.py")
    #Execute instruction
    os.system("python3 /home/cylaunch/payload_code/execute_instruction.py " + instruction_string)
    create_file(EXECUTE_INSTRUCTION_F)
    log.writeTo("Exited " + __name__)

def completed_cleanup_state():
    log.writeTo("Entered " + __name__)
    log.writeTo("Hard stopping stepper motors")
    os.system("python3 /home/cylaunch/payload_code/stopstep.py")



def create_file(path):
    os.system("touch " + path)

def get_pid(name):
    return map(int,check_output(["pidof",name]).split())    

if __name__ == "__main__":
        main()