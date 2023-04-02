from move import move
import time


def main():
    while True == True:
        userInput = input("What motor do you want? (S for stepper L for lin act) ")
        userDir = input("F or B? ")
        userSteps = int(input("How many steps: "))
        if userInput == "S":
            if userDir == "F":
                move.spinF(userSteps)
            elif userDir == "B":
                move.spinB(userSteps)
        elif userInput == "L":
            if userDir == "F":
                move.extendF(userSteps)
            elif userDir == "B":
                move.extendB(userSteps)
        time.sleep(2)


if __name__ == "__main__":
    main()
