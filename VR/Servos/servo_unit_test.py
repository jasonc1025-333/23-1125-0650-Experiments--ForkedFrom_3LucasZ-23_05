import servo_controller as sc

class msg:
	def __init__(self, data):
		self.data = data

msg1 = msg(True)
msg2 = msg(50)
sc.callback_servoPWR_enable(msg1)
sc.callback_servo0_enable(msg1)
sc.callback_servo0_angle(msg2)