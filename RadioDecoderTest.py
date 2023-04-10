from RadioDecoder import RadioDecoder
import os
import time

PATH = "/home/cylaunch/payload_code/radio_output/empty.txt"

def main():
    while(os.path.getsize(PATH) == 0):
        print("ZZZZ")
        time.sleep(1)
    decoder = RadioDecoder(PATH)
    decoder.decode64()
    print(decoder.FinalString)

if __name__ == "__main__":
    main()