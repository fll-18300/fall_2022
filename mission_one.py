import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_one(r):
    print("Running Mission 1")
    #Lydia and Madeleine 
    r.ev3.screen.draw_text(30, 60, "Mission 1")
    r.robot.straight(600)
    r.left_attachment_motor.run(200) 
    wait(1000)
    r.left_attachment_motor.stop()
    r.ev3.screen.clear()