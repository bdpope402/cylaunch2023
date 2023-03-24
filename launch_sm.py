import rocketcheck
import execute_instruction
import time
import os

WAIT_TIME = 1800 #30 minute sleep time
SLEEP_FILE_PATH = "/home/cylaunch/payload_code/flags/dosleep.cyl"

def main():
    print("In main")
    if(os.path.exists(SLEEP_FILE_PATH) == False):
        print("Entering launchpad sleep")
        time.sleep(WAIT_TIME)
    else:
        print("skipping launchpad sleep")
    while(rocketcheck.checkIfLaunching() == False):
        time.sleep(1)
    print("Exited while loop")


if __name__ == "__main__":
    main()
