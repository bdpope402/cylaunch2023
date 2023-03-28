# Importing the library needed for decoding the radio data from base 64
import base64

# opening the file with the radio data and reading the data
radiofile = open("radio_recieved_transmission.txt", "r+")
RadioOutput = radiofile.read()
radiofile.close()

#decoding the radio data from base 64 to bytes
DecodeString = base64.b64decode(RadioOutput)
#changing the decoded radio data to a string
DecodeString = str(DecodeString)
#getting the length of the string with the radio data
length = len(DecodeString)

#getting rid of the extra add on's from the byte format
DecodeString = DecodeString[2:length-1]
length = len(DecodeString)

#printing the final string from NASA before editing it
##print(DecodeString)

#code to create a string with the call sign and the commands

#finding the end of the call sign
count = 0
for i in DecodeString:
    if(i == ">"):
        index = count
        break
    count = count + 1

#string containing the call sign
CallSign = DecodeString[0:index]

#finding the beginning of the commands
count = 0
for i in DecodeString:
    if(i == "A" or i == "B" or i == "C"):
        tempindex = count
        if(DecodeString[tempindex + 1:tempindex + 2] == "1" or DecodeString[tempindex + 1:tempindex + 2] == "2" or DecodeString[tempindex + 1:tempindex + 2] == "3"):
            index2 = count
            break
    count = count + 1

#finding the end of the commands
count = 0
for i in DecodeString:
    if(i == "_"):
        index3 = count
        break
    count = count + 1

#a string made to contain all of the commands
Commands = DecodeString[index2:index3]

#creates a final string
FinalString = CallSign + " " + Commands

#prints the final string
print(FinalString)
