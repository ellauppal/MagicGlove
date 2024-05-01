from camera_detect import *
from colour_detect import *
from range_sensor import *
from gcp_text2speech import *
from light_detection import *
import RPi.GPIO as GPIO
import time

def main():
    # gcp
    audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"
    image_file = "/home/magicglove/MagicGlove/test/image.jpg"

    # interfacing gpio
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    BUTTON_POWER = 10
    BUTTON_COLOR_DETECT = 9
    BUTTON_SPATIAL_REC = 11
    BUTTON_LIGHT_INTENSE = 0

    # pin 9,10,11 & 0 is input pin and set intial value to be pulled low (off)
    GPIO.setup(BUTTON_POWER, GPIO.IN)
    GPIO.setup(BUTTON_COLOR_DETECT, GPIO.IN)
    GPIO.setup(BUTTON_SPATIAL_REC, GPIO.IN)
    GPIO.setup(BUTTON_LIGHT_INTENSE, GPIO.IN)

    # main Loop for the device
    while (True):
        print("Device started")
        # intalize
        power = False
        colorStatus = False
        spatialStatus = False
        lightStatus = False

        diff = 0
        while (diff < 0.2):
            while (GPIO.input(BUTTON_POWER) != GPIO.HIGH): pass
            last = time.time()
            while (GPIO.input(BUTTON_POWER) != GPIO.LOW): pass
            diff = time.time() - last
        power = True
        speech_to_text("Power on.", audio_file)

        while (power):
            diff = 0
            while ((GPIO.input(BUTTON_POWER) != GPIO.HIGH) and (GPIO.input(BUTTON_COLOR_DETECT) != GPIO.HIGH) and (GPIO.input(BUTTON_SPATIAL_REC) != GPIO.HIGH) and (GPIO.input(BUTTON_LIGHT_INTENSE) != GPIO.HIGH)): pass
            if (GPIO.input(BUTTON_POWER) == GPIO.HIGH):
                print("POWER")
                last = time.time()
                while (GPIO.input(BUTTON_POWER) == GPIO.HIGH): pass
                diff = time.time() - last
                if (diff > 0.2):
                    power = False
            elif (GPIO.input(BUTTON_COLOR_DETECT) == GPIO.HIGH):
                print("COLOR")
                last = time.time()
                while (GPIO.input(BUTTON_COLOR_DETECT) == GPIO.HIGH): pass
                diff = time.time() - last
                if (diff > 0.2):
                    colorStatus = True
            elif (GPIO.input(BUTTON_SPATIAL_REC) == GPIO.HIGH):
                print("SPATIAL")
                last = time.time()
                while (GPIO.input(BUTTON_SPATIAL_REC) == GPIO.HIGH): pass
                diff = time.time() - last
                if (diff > 0.2):
                    spatialStatus = True
            elif (GPIO.input(BUTTON_LIGHT_INTENSE) == GPIO.HIGH):
                print("LIGHT")
                last = time.time()
                while (GPIO.input(BUTTON_LIGHT_INTENSE) == GPIO.HIGH): pass
                diff = time.time() - last
                if (diff > 0.2):
                    lightStatus = True

            if (diff < 0.2):
                continue

            if (not power):
                break
            elif (colorStatus):
                speech_to_text("Colour detection on.", audio_file)
                # get image
                image_capture(image_file)
                # run colour detect on image and get colour
                recent_colour = colour_detect_on_image(image_file)
                print(recent_colour)
                colorStatus = False
                # call gcp
                speech_to_text(f"The colour is {recent_colour}", audio_file)
            elif (spatialStatus):
                speech_to_text("Spatial recognition on.", audio_file)
                call_range_sensor()
                spatialStatus = False
            elif (lightStatus):
                print('Entered the light thread')
                speech_to_text("Light detection on.", audio_file)
                if calling_light_sensor() == True:
                    speech_to_text("The lights are on", audio_file)
                else:
                    speech_to_text("The lights are off", audio_file)

                lightStatus = False

        print("Power Off")
        speech_to_text("Power off", audio_file)

if __name__ == "__main__":
    main()
