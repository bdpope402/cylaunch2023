#----------------------------------------------------
# Manual loop for extending / retracting stepper motors
# Stepper 1 is body rotation motor, 1.8° per step, 3.6° per doublestep
# Stepper 2 is linear actuator, .0018 mm per step, .0038 mm per doublestep
#----------------------------------------------------
from move import move
import time

def main():
    move_local = move()
    while True == True:
        userInput = input("What motor do you want? (S for stepper L for lin act, E to exit) ")
        if(userInput.upper() == "E"):
            move_local.releaseStepper()
            move_local.releaseLin()
            break
        userDir = input("F or B? ")
        userSteps = int(input("How many steps (angle for stepper motor): "))
        if userInput == "S":
            if userDir == "F":
                move_local.spinF(userSteps)
            elif userDir == "B":
                move_local.spinB(userSteps)
        elif userInput == "L":
            if userDir == "F":
                move_local.extendF(userSteps)
            elif userDir == "B":
                move_local.extendB(userSteps)
        time.sleep(2)


if __name__ == "__main__":
    main()
