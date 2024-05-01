import RPi.GPIO as GPIO
import time

def light_intensity():
    count = 0
    ldr = 4 
    count = 0
    delayt = 0.1
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(delayt)
    GPIO.setup(ldr, GPIO.IN)
  
    # count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        count += 1

    return count

def calling_light_sensor():
    timeout = 2 # [seconds]
    timeout_start = time.time()
    while (True and time.time() < timeout_start + timeout):
            store = light_intensity()
    
    if ( store <= 200 ):
            print("Lights are ON")
            return True
    else:
        print("Lights are OFF")
        return False
    

if __name__ == "__main__":
    calling_light_sensor() # for testing