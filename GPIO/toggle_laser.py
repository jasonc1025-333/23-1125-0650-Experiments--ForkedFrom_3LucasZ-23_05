import RPi.GPIO as GPIO
import time

PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)
print("POWER SUPPLIED")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(2)
print("POWER OFF")
GPIO.output(PIN, GPIO.LOW)
