import RPi.GPIO as GPIO
import math
import time
import servo_settings 
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

bus = smbus.SMBus(1)		#this is I2C1 on the pi4
DEVICE_ADDRESS = 0x40 		#Address of the PCA9685 IC
		
servoPowerEnabled = False	#start with the servos powered off

servo_enabled	 = [True] * 16	#start with all the individuall servos enabled for movement
servo_saved_angle= [0] *16

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
		print("here")
		angle = constrain(angle, 0, servo_settings.servo_max_angle[channel])
		servo_saved_angle[channel] = angle
		onCount  = 0
		offPulse = map(angle,0,servo_settings.servo_max_angle[channel],servo_settings.servo_min_pulse[channel],servo_settings.servo_max_pulse[channel])		#map the angle to pulse length
		offCount = map(offPulse,0,20000,0,4095)		#map the pulse length to register value
		offCount = int(constrain(offCount,0,4095))
		set_pwm(channel,onCount,offCount)
		
def set_pwm(channel, on, off):
	try:
		print("here2")
		bus.write_byte_data(DEVICE_ADDRESS, LED0_ON_L+4*channel, on & 0xFF)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_ON_H+4*channel, on >> 8)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_OFF_L+4*channel, off & 0xFF)
		bus.write_byte_data(DEVICE_ADDRESS, LED0_OFF_H+4*channel, off >> 8)
	except Exception as e:
		print("except on set_pwm")
		print(e)


def callback_servo0_angle(msg):
	servo(0,msg.data)
def callback_servo1_angle(msg):
	servo(1,msg.data)
def callback_servo2_angle(msg):
	servo(2,msg.data)
def callback_servo3_angle(msg):
	servo(3,msg.data)
def callback_servo4_angle(msg):
	servo(4,msg.data)
def callback_servo5_angle(msg):
	servo(5,msg.data)
def callback_servo6_angle(msg):
	servo(6,msg.data)
def callback_servo7_angle(msg):
	servo(7,msg.data)
def callback_servo8_angle(msg):
	servo(8,msg.data)
def callback_servo9_angle(msg):
	servo(9,msg.data)
def callback_servo10_angle(msg):
	servo(10,msg.data)
def callback_servo11_angle(msg):
	servo(11,msg.data)
def callback_servo12_angle(msg):
	servo(12,msg.data)
def callback_servo13_angle(msg):
	servo(13,msg.data)
def callback_servo14_angle(msg):
	servo(14,msg.data)
def callback_servo15_angle(msg):
	servo(15,msg.data)

def callback_servo0_enable(msg):
	if msg.data == True:
		servoEnable(0)
	else:
		servoDisable(0)	
def callback_servo1_enable(msg):
	if msg.data == True:
		servoEnable(1)
	else:
		servoDisable(1)
def callback_servo2_enable(msg):
	if msg.data == True:
		servoEnable(2)
	else:
		servoDisable(2)
def callback_servo3_enable(msg):
	if msg.data == True:
		servoEnable(3)
	else:
		servoDisable(3)
def callback_servo4_enable(msg):
	if msg.data == True:
		servoEnable(4)
	else:
		servoDisable(4)
def callback_servo5_enable(msg):
	if msg.data == True:
		servoEnable(5)
	else:
		servoDisable(5)
def callback_servo6_enable(msg):
	if msg.data == True:
		servoEnable(6)
	else:
		servoDisable(6)
def callback_servo7_enable(msg):
	if msg.data == True:
		servoEnable(7)
	else:
		servoDisable(7)
def callback_servo8_enable(msg):
	if msg.data == True:
		servoEnable(8)
	else:
		servoDisable(8)
def callback_servo9_enable(msg):
	if msg.data == True:
		servoEnable(9)
	else:
		servoDisable(9)
def callback_servo10_enable(msg):
	if msg.data == True:
		servoEnable(10)
	else:
		servoDisable(10)
def callback_servo11_enable(msg):
	if msg.data == True:
		servoEnable(11)
	else:
		servoDisable(11)
def callback_servo12_enable(msg):
	if msg.data == True:
		servoEnable(12)
	else:
		servoDisable(12)
def callback_servo13_enable(msg):
	if msg.data == True:
		servoEnable(13)
	else:
		servoDisable(13)
def callback_servo14_enable(msg):
	if msg.data == True:
		servoEnable(14)
	else:
		servoDisable(14)
def callback_servo15_enable(msg):
	if msg.data == True:
		servoEnable(15)
	else:
		servoDisable(15)

def callback_servoPWR_enable(msg):
	if msg.data == True:
		powerEnable()
	else:
		powerDisable()

#setup the pin that controls the power to the servo and driver chip
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

class msg:
	def __init__(self, data):
		self.data = data

msg1 = msg(True)
msg2 = msg(50)
callback_servoPWR_enable(msg1)
callback_servo0_enable(msg1)
callback_servo0_angle(msg2)

#GPIO.cleanup()
