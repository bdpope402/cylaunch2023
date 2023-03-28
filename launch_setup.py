import os
from datetime import datetime

SKIP_SLEEP_PATH = "/home/cylaunch/payload_code/flags/skipSleep.cyl"
SKIP_SM_PATH= "/home/cylaunch/payload_code/flags/SkipSM.cyl"

now = datetime.now()

def main():
    while(True):
        userInput = input("Start launch state machine on next restart?(Y/N)")
        if(userInput.upper() == "N"):
            os.system("touch " + SKIP_SM_PATH)
            break
        elif(userInput.upper() == "Y"):
            os.system("rm "+ SKIP_SM_PATH)
            break
        print("Invalid input, put either Y or N")
    while(True):
        userInput = input("Do 30 minute accelerometer input delay before launch? (Y/N)")
        if(userInput.upper() == "N"):
            os.system("touch " + SKIP_SLEEP_PATH)
            break
        elif(userInput.upper() == "Y"):
            os.system("rm " + SKIP_SLEEP_PATH)
            break
        print("Invalid input, put either Y or N")
    print("Moving old logfiles to /home/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))
    os.system("mkdir /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))
    os.system("mv -v /home/cylaunch/payload_code/logs/* /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))

    # while(True):
    #     userInput = input


if __name__ == "__main__":
    main()
