import socket

#config
MY_ADDR = ("", 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

while True:
    data, addr = sock.recvfrom(4)
    print("(", data[0], ",", data[1], ")")