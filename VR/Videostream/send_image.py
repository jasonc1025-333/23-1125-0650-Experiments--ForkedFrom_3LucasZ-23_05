import socket
import cv2
import time

#config
#mac
#OTHER_ADDR = ("192.168.1.144", 5000)
#vr
OTHER_ADDR = ("192.168.1.178", 5000)
#sudo sysctl -w net.inet.udp.maxdgram=65535

#setup
camera = cv2.VideoCapture(0)
camera.set(3, 256)
camera.set(4, 256)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#run
time.sleep(1)
print("Send image begun!")
currentTime = time.time()
while True:
    prevTime = currentTime
    currentTime = time.time()
    #print("frame time:", currentTime - prevTime)
    retval, frame = camera.read()
    frame = cv2.flip(frame, -1)
    retval, jpg = cv2.imencode('.jpg', frame)
    sock.sendto(jpg, OTHER_ADDR)
