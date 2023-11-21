#
# servo_settings.py
# Cory Duce cory.duce@gmail.com
# Nov 24 2020
# 
# v1.0 -Initial release
#


# jwc 23-1120-1550 appears that LEGO Green Servo Motors: 600/2400 is best (400 too low and causes issue)
#User adjustable parameters for the 16 servo channels
#
#
#   				0	  1     2     3     4     5     6     7     8     9     10    11    12    13    14    15
servo_max_angle  = [180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180,  180  ]
###jwc o servo_min_pulse  = [400,  400,  500,  600,  600,  600,  600,  400,  600,  600,  600,  600,  600,  600,  600,  600  ]
servo_min_pulse  = [600,  600,  600,  600,  600,  600,  600,  400,  600,  600,  600,  600,  600,  600,  600,  600  ]
###jwc o servo_max_pulse  = [2600, 2600, 2400, 2400, 2400, 2400, 2400, 2600, 2600, 2400, 2400, 2400, 2400, 2400, 2400, 2400 ]
servo_max_pulse  = [2400, 2400, 2400, 2400, 2400, 2400, 2400, 2600, 2600, 2400, 2400, 2400, 2400, 2400, 2400, 2400 ]
###jwc o servo_init_angle = [0,    180,   0,   90,   90,   90,   90,   0,   180,   90,   90,   180,   90,   90,   90,   90   ]
servo_init_angle = [90,   90,   90,   90,   90,   90,   90,   0,   180,   90,   90,   180,   90,   90,   90,   90   ]
servo_init_delay = [0,    0.05,    0.10,  0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75 ]
