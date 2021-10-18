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
def profile(servoId, servoAngle):
    if servoId == 0:
		sc.callback_servo0_enable(trueMsg)
		angle = sc.msg(servoAngle)
		sc.callback_servo0_angle(angle)
	elif servoId == 1:
		sc.callback_servo1_enable(trueMsg)
		angle = sc.msg(servoAngle)
		sc.callback_servo1_angle(angle)
	return url_for('main')