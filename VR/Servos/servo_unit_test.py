# jwc 24-0506-0730 TYJ Works 
##  '/0/0' '/0/90' '/0/180' Left_Servo
##  '/1/0' '/1/90' '/1/180' Right_Servo
##  TYJ LEGO TECHNIC Green Servo *Continuous) Works w/o extra power source needed, just using RPi Power
##  0 to 180 degrees on protractor from perspective of bystander outside of vehicle (non-driver)

from flask import Flask, url_for
import servo_controller as sc

app = Flask(__name__)

trueMsg = sc.msg(True)
falseMsg = sc.msg(False)

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

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
