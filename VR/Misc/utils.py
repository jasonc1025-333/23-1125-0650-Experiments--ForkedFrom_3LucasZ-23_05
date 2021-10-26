import motor_controller as mc
import servo_controller as sc

def reset():
    mc.set_to(0, 0)
    pan_angle = sc.msg(56)
    tilt_angle = sc.msg(130)
    sc.callback_servo0_angle(pan_angle)
    sc.callback_servo1_angle(tilt_angle)