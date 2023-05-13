import RPi.GPIO as GPIO
import time

PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

ON=False

while True:
  res = input("Toggle")
  if res=="":
    ON=not ON
    if ON:
      print("POWER SUPPLIED")
      GPIO.output(PIN, GPIO.HIGH)
    else:
      print("POWER OFF")
      GPIO.output(PIN, GPIO.LOW)
