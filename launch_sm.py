import rocketcheck
import execute_instruction
import time
import os
from cyllogger import cyllogger 
import hat_test

WAIT_TIME = 1800 #30 minute sleep time
IN_FLIGHT_TIME = 180 # 3 minute flight
SKIP_SLEEP_PATH = "/home/cylaunch/payload_code/flags/skipSleep.cyl"
SKIP_SM_PATH= "/home/cylaunch/payload_code/flags/SkipSM.cyl"

log = cyllogger("sm_log")

def main():
    log.writeTo("Entered main() of launch_sm")
    if(os.path.exists(SKIP_SLEEP_PATH) == False):
        log.writeTo(f"Entering launchpad sleep, sleeping for: {str(WAIT_TIME/60)} minutes.")
        time.sleep(WAIT_TIME)
    else:
        log.writeTo("skipSleep.cyl exists, immediately checking accelerometer data")
    while(rocketcheck.checkIfLaunching() == False):
        time.sleep(1)
    log.writeTo("Exited launch loop")
    time.sleep(IN_FLIGHT_TIME) #Sleep for 3 minutes to accomodate launch
    log.writeTo("Starting landed loop")
    while(rocketcheck.checkIfLanded() == False):
        time.sleep(1)
    log.writeTo("Exited landing loop")

    #find upright door, launch fm_rtl and multimon


if __name__ == "__main__":
    if(os.path.exists(SKIP_SM_PATH) == True):
        log.writeTo("skipSM.cyl found, not entering main()")
    else:
        main()
