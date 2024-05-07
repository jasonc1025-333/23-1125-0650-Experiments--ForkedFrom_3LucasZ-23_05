# jwc 24-0506-0730 TYJ Works 
# jwc y Create 'symbolic_link' to access a local_library_folder 'Servos': 23-1207-1325: from Servos import servo_settings 
# jwc Created 'ln -sv ../Servos/ ./Servos'
#
#  '/0/0' '/0/90' '/0/180' Left_Servo
#  '/1/0' '/1/90' '/1/180' Right_Servo
#  TYJ LEGO TECHNIC Green Servo *Continuous) Works w/o extra power source needed, just using RPi Power
#  0 to 180 degrees on protractor from perspective of bystander outside of vehicle (non-driver)

from flask import Flask, url_for
import servo_controller as sc

app = Flask(__name__)

trueMsg = sc.msg(True)
falseMsg = sc.msg(False)

servoLeft_Id = 0
servoRight_Id = 1

Angle_000_Degrees_ServoControllerMsg = sc.msg(int(0))
Angle_090_Degrees_ServoControllerMsg = sc.msg(int(90))
Angle_180_Degrees_ServoControllerMsg = sc.msg(int(180))

sc.callback_servoPWR_enable(trueMsg)

@app.route("/")
def main():
    return "Please enter something like: /0/40"

@app.route('/<servoId>/<servoAngle>')
def move_servo(servoId, servoAngle):
    sc.callback_servo_enable(int(servoId), trueMsg)
    angle = sc.msg(int(servoAngle))
    sc.callback_servo_angle(int(servoId),angle)
    return ('id: ' + servoId + ' angle: ' + servoAngle)

@app.route("/on")
def board_on():
    sc.callback_servoPWR_enable(trueMsg)
    return ('board on')

@app.route("/off")
def board_off():
    sc.callback_servoPWR_enable(falseMsg)
    return ('board off')

@app.route("/f")
def motion_forward():
    sc.callback_servo_enable(servoLeft_Id, trueMsg)
    sc.callback_servo_enable(servoRight_Id, trueMsg)
    sc.callback_servo_angle(servoLeft_Id,Angle_180_Degrees_ServoControllerMsg)
    sc.callback_servo_angle(servoRight_Id,Angle_000_Degrees_ServoControllerMsg)	
    return ('motion_forward')

@app.route("/s")
def motion_stop():
    sc.callback_servo_enable(servoLeft_Id, trueMsg)
    sc.callback_servo_enable(servoRight_Id, trueMsg)
    sc.callback_servo_angle(servoLeft_Id,Angle_090_Degrees_ServoControllerMsg)
    sc.callback_servo_angle(servoRight_Id,Angle_090_Degrees_ServoControllerMsg)	
    return ('motion_stop')

@app.route("/b")
def motion_backward():
    sc.callback_servo_enable(servoLeft_Id, trueMsg)
    sc.callback_servo_enable(servoRight_Id, trueMsg)
    sc.callback_servo_angle(servoLeft_Id,Angle_000_Degrees_ServoControllerMsg)
    sc.callback_servo_angle(servoRight_Id,Angle_180_Degrees_ServoControllerMsg)	
    return ('motion_backward')

@app.route("/l")
def motion_left():
    sc.callback_servo_enable(servoLeft_Id, trueMsg)
    sc.callback_servo_enable(servoRight_Id, trueMsg)
    sc.callback_servo_angle(servoLeft_Id,Angle_000_Degrees_ServoControllerMsg)
    sc.callback_servo_angle(servoRight_Id,Angle_000_Degrees_ServoControllerMsg)	
    return ('motion_left')

@app.route("/r")
def motion_right():
    sc.callback_servo_enable(servoLeft_Id, trueMsg)
    sc.callback_servo_enable(servoRight_Id, trueMsg)
    sc.callback_servo_angle(servoLeft_Id,Angle_180_Degrees_ServoControllerMsg)
    sc.callback_servo_angle(servoRight_Id,Angle_180_Degrees_ServoControllerMsg)	
    return ('motion_right')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
