python3 Servos/receive_servo.py &
PID_ONE=$!
python3 Videostream/send_image.py & 
PID_TWO=$!
python3 Drivetrain/receive_motor.py &
PID_THREE=$!
python3 Misc/ping_listen.py &
PID_FOUR=$!