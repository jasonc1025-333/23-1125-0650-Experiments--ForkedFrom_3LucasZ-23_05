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
    left = int.from_bytes(bytes(data[0]), "big", signed=True)
    right = int.from_bytes(bytes(data[1]), "big", signed=True)
    print("Motors: (", left, ",", right, ")")
    mc.set_to(left, right)
