import socket
import motor_controller as mc
from Misc import config

#config
MY_ADDR = (config.BOT_IP, config.BOT_MOTOR_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

mc.on()
print("Receive motor begun!")
while True:
    data, addr = sock.recvfrom(4)
    left = data[0] - 127
    right = data[1] - 127
    print("Motors: (", left, ",", right, ")")
    mc.set_to(left, right)
