import RPi.GPIO as GPIO
import smbus2 as smbus
import time
from textwrap import wrap

#setup
I2C_PIN = 17
BUS = smbus.SMBus(6)
DEVICE_ADDRESS = 0x53
LEFT_MOTOR = 3
RIGHT_MOTOR = 4
GPIO.setmode(GPIO.BCM)
time.sleep(0.1)
GPIO.setup(I2C_PIN, GPIO.OUT)

def off():
    set_to(0, 0)
    GPIO.output(I2C_PIN, GPIO.LOW)

def on():
    GPIO.output(I2C_PIN, GPIO.HIGH)


def set_to(left, right, verbose=False):
    BUS.write_i2c_block_data(DEVICE_ADDRESS, LEFT_MOTOR, int_to_byte_array(normalize(left)))
    BUS.write_i2c_block_data(DEVICE_ADDRESS, RIGHT_MOTOR, int_to_byte_array(normalize(right)))
    if verbose:
        print("Left:", left)
        print("Right:", right)

def int_to_byte_array(num):
   if num < 0:
      hexStr = hex((1<<32) + num)
   else:
      hexStr = hex(num)
   hexStr = hexStr.rstrip("L")

   padded = str.format('{:08X}',int(hexStr,16))
   padded = wrap(padded,2)

   array = [0,0,0,0]
   for x in range(4):
      array[x] = int(padded[x],16)

   array.reverse()
   return array

def normalize(num):
    THRESHOLD = 255
    return max(min(num, THRESHOLD), -1 * THRESHOLD)
