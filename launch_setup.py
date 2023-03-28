import os
from datetime import datetime

SLEEP_FILE_PATH = "/home/cylaunch/payload_code/flags/dosleep.cyl"
SM_FILE_PATH= "/home/cylaunch/payload_code/flags/doLaunchOnStartup.cyl"

now = datetime.now()

def main():
    while(True):
        userInput = input("Start launch state machine on next restart?(Y/N)")
        if(userInput.upper() == "Y"):
            os.system("touch " + SM_FILE_PATH)
            break
        elif(userInput.upper() == "N"):
            os.system("rm "+ SM_FILE_PATH)
            break
        print("Invalid input, put either Y or N")
    while(True):
        userInput = input("Do 30 minute accelerometer input delay before launch? (Y/N)")
        if(userInput.upper() == "Y"):
            os.system("touch " + SLEEP_FILE_PATH)
            break
        elif(userInput.upper() == "N"):
            os.system("rm " + SLEEP_FILE_PATH)
            break
        print("Invalid input, put either Y or N")
    print("Moving old logfiles to /home/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))
    os.system("mkdir /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))
    os.system("mv -v /home/cylaunch/payload_code/logs/* /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M"))

    # while(True):
    #     userInput = input


if __name__ == "__main__":
    main()
