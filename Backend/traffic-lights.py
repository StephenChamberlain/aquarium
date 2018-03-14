import RPi.GPIO as GPIO
import time
# ---------------------------------

gpioPinRed = 4
gpioPinYellow = 17
gpioPinGreen = 22

delay = 1

def switchPins(red, yellow, green):
    GPIO.output(gpioPinRed, red)
    GPIO.output(gpioPinYellow, yellow)
    GPIO.output(gpioPinGreen, green)

# ---------------------------------
print("About to activate traffic lights...")

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioPinRed, GPIO.OUT)
GPIO.setup(gpioPinYellow, GPIO.OUT)
GPIO.setup(gpioPinGreen, GPIO.OUT)

# ---------------------------------
print("Possible cleanup from earlier runs")
switchPins(False, False, False)

# ---------------------------------
print("Red to green flow")
switchPins(True, False, False)
time.sleep(delay)
switchPins(True, True, False)
time.sleep(delay)
switchPins(False, False, True)
time.sleep(delay)

# ---------------------------------
print("Cleanup and terminate")
switchPins(False, False, False)
GPIO.cleanup()