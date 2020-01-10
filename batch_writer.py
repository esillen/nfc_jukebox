from time import sleep
import sys
import label_writer

if __name__ == "__main__":
    filename = sys.argv[1]
    lines = filename.readlines()
    lines = [line.strip() for line in lines]
    
    try:
        for line in lines:
            filename = line
            print("Hold a tag near the reader")
            print("To write %s" % (filename))
            label_writer.write(filename)
            print("wrote %s to card!" % (filename))
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise