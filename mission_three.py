import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_three(r):
    #Lydia and Madeleine
    # Wind Turbine and Toy Factory
    print("Running Mission 3")
    r.ev3.screen.clear()
    r.robot.straight(500)
    r.robot.turn(-45)
    r.robot.straight(252)
    r.robot.turn(90)
    r.robot.straight(257)
    r.robot.straight(-53)
    wait(1000)
    r.robot.straight(45)
    r.robot.straight(-53)
    wait(1000)  
    r.robot.straight(53)