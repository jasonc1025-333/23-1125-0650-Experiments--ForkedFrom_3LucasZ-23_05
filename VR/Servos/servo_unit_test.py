import servo_controller as sc

msg1 = sc.msg(True)
msg2 = sc.msg(50)
sc.callback_servoPWR_enable(msg1)
sc.callback_servo0_enable(msg1)
sc.callback_servo0_angle(msg2)