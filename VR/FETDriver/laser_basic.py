import RPi.GPIO as GPIO
import time

PIN_DRIVER1 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_DRIVER1, GPIO.OUT)
GPIO.output(PIN_DRIVER1, GPIO.HIGH)
time.sleep(5)
GPIO.cleanup()
