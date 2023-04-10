import os
from datetime import datetime

SKIP_SLEEP_PATH = "/home/cylaunch/payload_code/flags/skipSleep.cyl"
SM_ON_RESTART= "/home/cylaunch/payload_code/flags/SMRestart.cyl"
RADIO_OUTPUT_PATH = "/home/cylaunch/payload_code/radio_output/empty.txt"

now = datetime.now()

def main():
    while(True):
        userInput = input("Restart SM on restart?")
        if(userInput.upper() == "Y"):
            os.system("touch " + SM_ON_RESTART)
            break
        elif(userInput.upper() == "N"):
            os.system("rm "+ SM_ON_RESTART)
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
    print("Moving old photos to /home/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/photos")
    os.system("mkdir /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/photos")
    os.system("mv -v /home/cylaunch/payload_code/photos/* /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/photos")
    print("Moving old radio output to /home/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/radio_output")
    os.system("mkdir /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/radio_output")
    os.system("mv -v /home/cylaunch/payload_code/radio_output/* /home/cylaunch/oldlogs/launch" + now.strftime("%m-%d-%y-%H:%M") + "/radio_output")
    print("Purging old launch flags")
    os.system("rm -r /home/cylaunch/payload_code/flags/launchFlags/*")



    # while(True):
    #     userInput = input


if __name__ == "__main__":
    main()
