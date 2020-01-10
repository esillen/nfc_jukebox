from time import sleep
import sys
from mfrc522 import SimpleMFRC522
nfc = SimpleMFRC522()

def write(filename):
    nfc.write(filename)

if __name__ == "__main__":
    try:
        while True:
            user_input = input("Text to print to card: ")
            print("Hold a tag near the writer")
            write(user_input)
            print("wrote %s to card!" % (filename))
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
