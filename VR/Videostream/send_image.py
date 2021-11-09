import socket
import cv2
import time
from Misc import config

OTHER_ADDR = (config.OPERATOR_IP, config.OPERATOR_CAMERA_PORT)

#setup
camera = cv2.VideoCapture(0)
camera.set(3, 256)
camera.set(4, 256)

MY_ADDR = (config.BOT_IP, config.BOT_CAMERA_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

#run
time.sleep(1)
print("Send image begun!")
currentTime = time.time()
while True:
    prevTime = currentTime
    currentTime = time.time()

    if config.VERBOSE:
        print("frame time:", currentTime - prevTime)
        
    retval, frame = camera.read()
    frame = cv2.flip(frame, -1)
    retval, jpg = cv2.imencode('.jpg', frame)
    sock.sendto(jpg, OTHER_ADDR)