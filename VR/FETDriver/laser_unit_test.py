from flask import Flask, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

PIN_DRIVER1 = 24
PIN_DRIVER2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_DRIVER1, GPIO.OUT)
GPIO.output(PIN_DRIVER1, GPIO.LOW)
GPIO.setup(PIN_DRIVER2, GPIO.OUT)
GPIO.output(PIN_DRIVER2, GPIO.LOW)

@app.route("/")
def main():
    return "FETDriver Unit Testing, please enter something like:/1/on"

@app.route('/<driver>/<status>')
def move_servo(driver, status):
    if driver == '1':
        if status == 'on':
            GPIO.output(PIN_DRIVER1, GPIO.HIGH)
        else:
            GPIO.output(PIN_DRIVER1, GPIO.LOW)
    elif driver == '2':
        if status == 'on':
            GPIO.output(PIN_DRIVER2, GPIO.HIGH)
        else:
            GPIO.output(PIN_DRIVER2, GPIO.LOW)
    return ('driver: ' + driver + ', status: ' + status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

