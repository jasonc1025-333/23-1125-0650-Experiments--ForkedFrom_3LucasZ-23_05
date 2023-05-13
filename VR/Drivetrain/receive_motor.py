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
    #fine tuning since robot motors are reversed and c# bytes are only positive
    left = -1 * (data[0] - 127)
    right = -1 * (data[1] - 127)

    if left > 90:
        left=250
    if right > 90:
        right=250

    mc.set_to(left, right)
    
    if config.VERBOSE:
        print("Motors: (", left, ",", right, ")")
