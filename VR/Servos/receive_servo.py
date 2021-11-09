import socket
import servo_controller as sc
from Misc import config

#config
MY_ADDR = (config.BOT_IP, config.BOT_SERVO_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

msg1 = sc.msg(True)
sc.callback_servoPWR_enable(msg1)
sc.callback_servo0_enable(msg1)
sc.callback_servo1_enable(msg1)

print("Receive servo begun!")
while True:
    data, addr = sock.recvfrom(4)
    pan_angle = sc.msg(data[0])
    tilt_angle = sc.msg(data[1])
    sc.callback_servo0_angle(pan_angle)
    sc.callback_servo1_angle(tilt_angle)
    
    if config.VERBOSE:
        print("Pantilt (", data[0], ",", data[1], ")")