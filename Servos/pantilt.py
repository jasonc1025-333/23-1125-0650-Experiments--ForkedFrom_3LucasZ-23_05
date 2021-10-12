import servo_controller

class msg:
	def __init__(self, data):
		self.data = data

msg1 = msg(True)
msg2 = msg(50)
callback_servoPWR_enable(msg1)
callback_servo0_enable(msg1)
callback_servo0_angle(msg2)

GPIO.cleanup()