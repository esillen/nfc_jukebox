from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

def read():
    id, text = reader.read()
    return id, text

if __name__ == "__main__":
    try:
        while True:
            print("Hold a tag near the reader")
            id, text = read()
            print("ID: %s\nText: %s" % (id,text))
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
        