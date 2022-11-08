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
    r.robot.straight(370)
    r.robot.straight(-70)
    r.robot.turn(-45)
    r.robot.straight(469)
    r.robot.turn(90)

    # Another way to do this is to drive forward for an amount of time
    # by using drive(speed,turn)
    for x in range(3):        
        r.robot.drive(200,0)  
        wait(500)
        r.robot.stop()
        wait(100)
        r.robot.drive(-200,0) 
        wait(500)
        r.robot.stop()
        wait(500)



  