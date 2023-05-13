import servo_controller as sc
import time

trueMsg = sc.msg(True)
falseMsg = sc.msg(False)

sc.callback_servoPWR_enable(trueMsg)

ON=False

while True:
  res=input("TOGGLE")
  ON=not ON
  if ON:
    sc.servoEnable(8)
  else:
    sc.servoDisable(8)

sc.callback_servoPWR_enable(falseMsg)
