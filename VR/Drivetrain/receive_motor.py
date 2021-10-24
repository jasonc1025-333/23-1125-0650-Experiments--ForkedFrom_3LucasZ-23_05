import socket
import motor_controller as mc

#config
MY_ADDR = ("", 5001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

mc.on()
print("Receive motor begun!")
while True:
    data, addr = sock.recvfrom(4)
    print("Motors: (", data[0], ",", data[1], ")")
    mc.set_to(data[0], data[1])
