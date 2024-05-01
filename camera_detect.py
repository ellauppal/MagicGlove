from picamera2 import Picamera2
from time import sleep
from colour_detect import *

def image_capture(path):
    # when button is pressed
    camera = Picamera2()
    camera.start()
    sleep(2)
    camera.capture_file(path)
    print("FILE CAPTURED")
    camera.close()

if __name__ == "__main__":
    image_capture("/home/magicglove/MagicGlove/test/image.jpg")
    