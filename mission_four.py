import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_four(r):
    print("Running Mission 4")
    r.ev3.screen.draw_text(30, 60, "Mission 4")
    wait(1000)
    r.ev3.screen.clear()
    r.robot.straight(500)
    r.left_attachment_motor.stop(100)
    r.right_attachment_motor.stop(100) 
    r.robot.straight(-50)
    r.robot.turn(90)
    r.robot.striaght(600)
    r.robot.turn
