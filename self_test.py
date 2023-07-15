import os
import misc_tests.servoTurn as servoTurn
def main():
    print("Camera Detection Test:")
    print("-----------------------------\nOutput:")
    os.system("vcgencmd get_camera")
    print("-----------------------------")
    print("Verify that output is: supported=1 detected=1\n")
    print("If the output does not match, start by rebooting. Issue the command:\nsudo restart -r now\nCheck the cables from the raspberry pi to the camera and assure they are seated correctly. Retry this test after")
    input("Press enter to continue to the next test\n")
    print("RTL_SDR Detection Test:")
    print("-----------------------------\nOutput:")
    os.system("rtl_test -t")
    print("-----------------------------")
    print("Verify that it is detected and passes tests")
    input("Press enter to continue to the next test \n")
    print("Servo Movement test:")
    input("This code is meant to be run with the payload OUTSIDE of the rocket. press CTRL-C to exit the program, otherwise press enter to proceed")
    prettyPrint("Moving servo to 0 degrees")
    servoTurn.moveServo(0)
    input("Press enter to continue\n")
    prettyPrint("Moving servo to 135 degrees")
    servoTurn.moveServo(135)
    input("Press enter to continue\n")
    prettyPrint("Moving servo to 270 degrees")
    servoTurn.moveServo(270)
    print("Verify that it is detected and passes tests")
    input("Press enter to continue to the next test \n")

    
def prettyPrint(middleString):
    print("-----------------------------\nOutput:")
    print(middleString)
    print("-----------------------------")

if __name__ == "__main__":
    main()