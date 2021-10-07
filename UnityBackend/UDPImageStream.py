import socket
import cv2
import time
import base64

#config
MY_ADDR = ("192.168.1.144", 5001)
OTHER_ADDR = ("192.168.1.144", 5000)
#MY_ADDR = ("", 5000)
#OTHER_ADDR = ("192.168.1.139", 5000)

#setup
camera = cv2.VideoCapture(0)
camera.set(3, 120)
camera.set(4, 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
numSegments = 10
#run
print("sending started")
currentTime = time.time()
while True:
    prevTime = currentTime
    currentTime = time.time()
    print("frame time:", currentTime - prevTime)
    retval, frame = camera.read()
    retval, jpg = cv2.imencode('.jpg', frame)
    sock.sendto(jpg, OTHER_ADDR)