import cv2
import time 
import base64

camera = cv2.VideoCapture(0)
while True:
    retval, frame = camera.read()
    print("raw frame:", frame.shape)
    retval, frame = cv2.imencode('.jpg', frame)
    print("jpg frame:", frame.shape)
    #text = base64.b85encode(frame)
    #print("jpg text:", len(text))
    time.sleep(1)