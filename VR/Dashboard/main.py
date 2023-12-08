#IMPORTS
#websocket and flask
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit, send

#servos
###jwc o from Servos import servo_controller as sc
###jwc n from ../Servos/ import servo_controller as sc
###jwc n from ..Servos.servo_controller import servo_controller as sc
###jwc n import ../Servos/servo_controller as sc
###jwc n from ..Servos import servo_controller as sc
###jwc n from ..Servos.servo_controller import servo_controller as sc
###jwc n from ..Servos import servo_controller as sc
###jwc n from /home/jesus333/23-0921-1500-Jwc/23-1120-1300-Experiments--ForkedFrom_3LucasZ/Experiments--ForkedFrom_3LucasZ_/VR/Servos import servo_controller as sc

# jwc y Create 'symbolic_link' to access a local_library_folder 'Servos': 23-1207-1325: from Servos import servo_settings 
# jwc Created 'ln -sv ../Servos/ ./Servos'
from Servos import servo_controller as sc

#laser
import RPi.GPIO as GPIO

#misc
import time

#SETUP
#set up app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

#setup servo
trueMsg = sc.msg(True)
falseMsg = sc.msg(False)
ARM_PIN = 5
DIG_PIN = 14
speed = 5
sc.callback_servoPWR_enable(trueMsg)
sc.callback_servo_enable(ARM_PIN, trueMsg)
sc.callback_servo_enable(DIG_PIN, trueMsg)
armAngle = 90
sc.callback_servo_angle(ARM_PIN, sc.msg(armAngle))
digAngle = 90
sc.callback_servo_angle(DIG_PIN, sc.msg(digAngle))

def clamp(val):
    if (val<0):
        return 0
    if (val>180):
        return 180
    return val

#setup laser
laser_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(laser_pin, GPIO.OUT)
GPIO.output(laser_pin, GPIO.LOW)
laser_on = False

#COMMAND LISTENERS
@socketio.on('connect')
def connect():
    print('A client connected.')


@socketio.on('disconnect')
def disconnect():
    print('A client disconnected.')


@socketio.on('digDown')
def digDown():
    global digAngle
    digAngle = clamp(digAngle - speed)
    s = sc.msg(digAngle)
    sc.callback_servo_angle(DIG_PIN, s)
    print("dig:", digAngle)


@socketio.on('digUp')
def digUp():
    global digAngle
    digAngle = clamp(digAngle + speed)
    s = sc.msg(digAngle)
    sc.callback_servo_angle(DIG_PIN, s)
    print("dig:", digAngle)


@socketio.on('armDown')
def armDown():
    ###jwc o global armAngle
    ###jwc o armAngle = clamp(armAngle - speed)
    ###jwc o s = sc.msg(armAngle)
    ###jwc o sc.callback_servo_angle(ARM_PIN, s)
    ###jwc o print("arm", armAngle)

    servoId = 0
    servoAngle = 90
    
    sc.callback_servo_enable(int(servoId), trueMsg)
    
    angle = sc.msg(int(servoAngle))
    sc.callback_servo_angle(int(servoId),angle)
    ###jwc o print("arm", servoId, armAngle)
    print("arm_Down", servoId, servoAngle)
    
    ###jwc o return ('id: ' + servoId + ' angle: ' + servoAngle)
    return ('id: ' + str(servoId) + ' angle: ' + str(servoAngle))

    ###jwc o def move_servo(servoId, servoAngle):
    ###jwc o 	sc.callback_servo_enable(int(servoId), trueMsg)
    ###jwc o 	angle = sc.msg(int(servoAngle))
    ###jwc o 	sc.callback_servo_angle(int(servoId),angle)
    ###jwc o 	return ('id: ' + servoId + ' angle: ' + servoAngle)


@socketio.on('armUp')
def armUp():
    ###jwc o global armAngle
    ###jwc o armAngle = clamp(armAngle + speed)
    ###jwc o s = sc.msg(armAngle)
    ###jwc o sc.callback_servo_angle(ARM_PIN, s)
    ###jwc o print("arm", armAngle)

    servoId = 0
    servoAngle = 0

    sc.callback_servo_enable(int(servoId), trueMsg)
    
    angle = sc.msg(int(servoAngle))
    sc.callback_servo_angle(int(servoId),angle)
    ###jwc o print("arm", servoId, armAngle)
    print("arm_Up", servoId, servoAngle)
    
    ###jwc o return ('id: ' + servoId + ' angle: ' + servoAngle)
    return ('id: ' + str(servoId) + ' angle: ' + str(servoAngle))

    ###jwc o def move_servo(servoId, servoAngle):
    ###jwc o 	sc.callback_servo_enable(int(servoId), trueMsg)
    ###jwc o 	angle = sc.msg(int(servoAngle))
    ###jwc o 	sc.callback_servo_angle(int(servoId),angle)
    ###jwc o 	return ('id: ' + servoId + ' angle: ' + servoAngle)


@socketio.on('toggleLaser')
def toggleLaser():
    global laser_on
    laser_on = not laser_on
    if (laser_on):
        GPIO.output(laser_pin, GPIO.HIGH)
    else:
        GPIO.output(laser_pin, GPIO.LOW)
    print("laser:", laser_on)

#FLASK SERVING
#serve the webpage when a client connects to IP:5000
@app.route('/')
def home():
    return render_template('index.html')

#RUN THE APP
if __name__ == '__main__':
    print("ready for clients!")
    socketio.run(app, host='0.0.0.0', port=5000)

#PROGRAM CLEAN UP
GPIO.cleanup()