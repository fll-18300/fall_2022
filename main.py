#!/usr/bin/env pybricks-micropython

################################
# main.py
################################

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300
from menu import menu

###########
# Startup
###########
# Instantiate the Robot
r = robot_18300()

# Calibrate/Reset the Gyro to prevent drift
# COMMENT OUT TO SPEED UP TESTING!
r.calibrate_gyro(4)

# Program select menu
menu(r)