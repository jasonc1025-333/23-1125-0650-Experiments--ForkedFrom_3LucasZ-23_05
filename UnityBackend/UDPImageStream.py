import socket
import cv2
import time

#config
MY_ADDR = ("192.168.1.188", 5000)
OTHER_ADDR = ("192.168.1.144", 6000)
#MY_ADDR = ("", 5000)
#OTHER_ADDR = ("192.168.1.139", 5000)

#setup
camera = cv2.VideoCapture(0)
camera.set(3, 128)
camera.set(4, 128)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#run
print("wait for warm up...")
time.sleep(3)
print("sending started")
currentTime = time.time()
while True:
    prevTime = currentTime
    currentTime = time.time()
    print("frame time:", currentTime - prevTime)
    retval, frame = camera.read()
    frame = cv2.flip(frame, -1)
    retval, jpg = cv2.imencode('.jpg', frame)
    sock.sendto(jpg, OTHER_ADDR)