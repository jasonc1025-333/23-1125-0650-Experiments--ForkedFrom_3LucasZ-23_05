from flask import Flask, url_for
import motor_controller as mc

app = Flask(__name__)

@app.route("/")
def main():
    return "Please enter something like: /l/40"

@app.route('/<motorType>/<speed>')
def move_servo(motorType, speed):
    if motorType == 'l':
	    mc.set_to(int(speed), 0)
    elif motorType == 'r':
	    mc.set_to(0, int(speed))
    return ('motor: ' + motorType + ' speed: ' + speed)

@app.route("/on")
def board_on():
    mc.on()
    return ('motors on')

@app.route("/off")
def board_off():
    mc.off()
    return ('motors off')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)