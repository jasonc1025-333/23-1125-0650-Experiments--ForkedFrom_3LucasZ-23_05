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
    if servoId == '0':
	    sc.callback_servo0_enable(trueMsg)
	    angle = sc.msg(int(servoAngle))
	    sc.callback_servo0_angle(angle)
    elif servoId == '1':
	    sc.callback_servo1_enable(trueMsg)
	    angle = sc.msg(int(servoAngle))
	    sc.callback_servo1_angle(angle)
    return ('id', servoId, 'angle', servoAngle)

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