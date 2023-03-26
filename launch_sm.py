import rocketcheck
import execute_instruction
import time
import os
from cyllogger import cyllogger 

WAIT_TIME = 1800 #30 minute sleep time
SLEEP_FILE_PATH = "/home/cylaunch/payload_code/flags/dosleep.cyl"
SM_FILE_PATH= "/home/cylaunch/payload_code/flags/doLaunchOnStartup.cyl"

log = cyllogger("sm_log")

def main():
    log.writeTo("In main")
    if(os.path.exists(SLEEP_FILE_PATH) == False):
        log.writeTo("Entering launchpad sleep")
        time.sleep(WAIT_TIME)
    else:
        log.writeTo("skipping launchpad sleep")
    while(rocketcheck.checkIfLaunching() == False):
        time.sleep(1)
    log.writeTo("Exited launch loop")
    time.sleep(5)
    log.writeTo("Starting landed loop")
    while(rocketcheck.checkIfLanded() == False):
        time.sleep(1)
    log.writeTo("Exited landing loop")

    #find upright door, launch fm_rtl and multimon


if __name__ == "__main__":
    if(os.path.exists(SLEEP_FILE_PATH) == True):
        main()
    else:
        log.writeTo("doLaunchOnStartup.cyl not found, not entering loop")
