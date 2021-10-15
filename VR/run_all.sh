python3 Servos/receive_servo.py &
PID_ONE=$!
python3 Videostream/send_image.py & 
PID_TWO=$!

