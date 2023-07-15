#----------------------------------------------------
# Class to decode and store the instruction string
#----------------------------------------------------
# Importing the library needed for decoding the radio data from base 64
import base64

DEFAULT_PATH = "/home/cylaunch/payload_code/radio_output/radio_recieved_transmission.txt"

class RadioDecoder:
    # opening the file with the radio data and reading the data
    def __init__(self, path):
        self.radiofile = open(path, "r+")
        self.RadioOutput = self.radiofile.read()
        self.radiofile.close()
        self.DecodeString = ""
        self.length = 0

    def decode64(self):
        #decoding the radio data from base 64 to bytes
        temp = base64.b64decode(self.RadioOutput)
    #changing the decoded radio data to a string
        self.DecodeString = str(temp)
    #getting the length of the string with the radio data
        self.length = len(self.DecodeString)

    #getting rid of the extra add on's from the byte format
        self.DecodeString = self.DecodeString[2:self.length-1]
        self.length = len(self.DecodeString)

    #printing the final string from NASA before editing it
    ##print(DecodeString)

    #code to create a string with the call sign and the commands

    #finding the end of the call sign
        count = 0
        for i in self.DecodeString:
            if(i == ">"):
                index = count
                break
            count = count + 1

    #string containing the call sign
        CallSign = self.DecodeString[0:index]
        self.callsign = CallSign

    #finding the beginning of the commands
        count = 0
        for i in self.DecodeString:
            if(i == "A" or i == "B" or i == "C"):
                tempindex = count
                if(self.DecodeString[tempindex + 1:tempindex + 2] == "1" or self.DecodeString[tempindex + 1:tempindex + 2] == "2" or self.DecodeString[tempindex + 1:tempindex + 2] == "3"):
                    index2 = count
                    break
            count = count + 1

        #finding the end of the commands
        count = 0
        for i in self.DecodeString:
            if(i == "_"):
                index3 = count
                break
            count = count + 1

        #a string made to contain all of the commands
        Commands = self.DecodeString[index2:index3]

        #creates a final string
        self.FinalString = CallSign + " " + Commands

        #prints the final string
        #print(self.FinalString)
