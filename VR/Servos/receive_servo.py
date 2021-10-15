import socket
import servo_controller as sc

#config
MY_ADDR = ("", 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)
ON_PI = True
if ON_PI:
    msg1 = sc.msg(True)
    sc.callback_servoPWR_enable(msg1)
    sc.callback_servo0_enable(msg1)
    sc.callback_servo2_enable(msg1)

while True:
    data, addr = sock.recvfrom(4)
    print("(", data[0], ",", data[1], ")")
    if (ON_PI):
        pan_angle = sc.msg(data[0])
        tilt_angle = sc.msg(data[1])
        sc.callback_servo0_angle(pan_angle)
        sc.callback_servo1_angle(tilt_angle)
