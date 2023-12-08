import RPi.GPIO as GPIO
import math
import time

###jwc o import servo_settings 
# jwc y Create 'symbolic_link' to access a local_library_folder 'Servos': 23-1207-1325: from Servos import servo_settings 
# jwc Created 'ln -sv ../Servos/ ./Servos'
from Servos import servo_settings 

import smbus2 as smbus

# Registers/etc:
PCA9685_ADDRESS    = 0x40
MODE1              = 0x00
MODE2              = 0x01
SUBADR1            = 0x02
SUBADR2            = 0x03
SUBADR3            = 0x04
PRESCALE           = 0xFE
LED0_ON_L          = 0x06
LED0_ON_H          = 0x07
LED0_OFF_L         = 0x08
LED0_OFF_H         = 0x09
ALL_LED_ON_L       = 0xFA
ALL_LED_ON_H       = 0xFB
ALL_LED_OFF_L      = 0xFC
ALL_LED_OFF_H      = 0xFD

# Bits:
RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04

###jwc o bus = smbus.SMBus(1)		#this is I2C1 on the pi4
###jwc n does go further but bad error: bus = smbus.SMBus(0)		#this is I2C1 on the pi4
# jwc 23-1208-0300 make sure do 'sudo raspi-config: enable i2c for SMBus:1'
bus = smbus.SMBus(1)		#this is I2C1 on the pi4

DEVICE_ADDRESS = 0x40 		#Address of the PCA9685 IC
		
servoPowerEnabled = False	#start with the servos powered off

servo_enabled	 = [True] * 16	#start with all the individuall servos enabled for movement
servo_saved_angle= [0] *16

class msg:
	def __init__(self, data):
		self.data = data
		
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def pca9685_init():
	try:
		bus.write_byte_data(DEVICE_ADDRESS,MODE2,OUTDRV)	#config outputs as totem pole
		time.sleep(0.05)  # wait for oscillator
		bus.write_byte_data(DEVICE_ADDRESS,PRESCALE,0x79)	#set frequency to 50hz
		time.sleep(0.05)  # wait for oscillator
		bus.write_byte_data(DEVICE_ADDRESS,MODE1,0x00)		#wake
		time.sleep(0.05)  # wait for oscillator
	except Exception as e:
		print(e)

	#set all servos to initial position
	for s in range(16):
		time.sleep(servo_settings.servo_init_delay[s])
		servo(s, servo_settings.servo_init_angle[s] )


def powerEnable():
	global servoPowerEnabled
	GPIO.output(23, GPIO.HIGH)
	time.sleep(0.5)		#supply takes time to start up
	servoPowerEnabled = True
	pca9685_init()

def powerDisable():
	global servoPowerEnabled
	GPIO.output(23, GPIO.LOW)
	servoPowerEnabled = False

def servoDisable(channel):
	global servo_enabled
	channel = constrain(channel,0,15)
	servo_enabled[channel] = False
	set_pwm(channel,0,0)

def servoEnable(channel):
	global servo_enabled
	channel = constrain(channel,0,15)
	servo_enabled[channel] = True
	servo(channel,servo_saved_angle[channel])

def servo(channel, angle):
	global servoPowerEnabled
	global servo_enabled
	global servo_saved_angle

	#print(channel)
	#print(servoPowerEnabled)
	#print(servo_enabled[channel])
	
	channel = constrain(channel,0,15)
	if( (servoPowerEnabled==True) and (servo_enabled[channel]==True) ):
		#print("here")
		angle = constrain(angle, 0, servo_settings.servo_max_angle[channel])
		servo_saved_angle[channel] = angle
		onCount  = 0
		offPulse = map(angle,0,servo_settings.servo_max_angle[channel],servo_settings.servo_min_pulse[channel],servo_settings.servo_max_pulse[channel])		#map the angle to pulse length
		offCount = map(offPulse,0,20000,0,4095)		#map the pulse length to register value
		offCount = int(constrain(offCount,0,4095))
		set_pwm(channel,onCount,offCount)
		
def set_pwm(channel, on, off):
	try:
		#print("here2")
		bus.write_byte_data(DEVICE_ADDRESS, LED0_ON_L+4*channel, on & 0xFF)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_ON_H+4*channel, on >> 8)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_OFF_L+4*channel, off & 0xFF)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_OFF_H+4*channel, off >> 8)
	except Exception as e:
		print("except on set_pwm")
		print(e)


def callback_servo_angle(id, msg):
	servo(id,msg.data)

def callback_servo_enable(id, msg):
	if msg.data == True:
		servoEnable(id)
	else:
		servoDisable(id)	

def callback_servoPWR_enable(msg):
	if msg.data == True:
		powerEnable()
	else:
		powerDisable()

#setup the pin that controls the power to the servo and driver chip
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
