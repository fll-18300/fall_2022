import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_eight(r):
    print("Running Mission 8")
    #John and Finn
    #Hydro,Innovation Project Circle, Smart Grid
    r.ev3.screen.clear()
    r.robot.straight(310)
    r.robot.turn(-45)
    # the robot goes straight and turns in front of the hydroelectric dam
    r.left_attachment_motor.run(-200)
   # the robot lets the attachment down to get ready to complete the hydroelectrc dam mission.
    r.robot.straight(130)
    r.left_attachment_motor.stop()
    r.robot.turn(-10)
    r.left_attachment_motor.run(200)
    # the robot uses the attachment to lift the bar and send the water down.
    wait(500)
    r.left_attachment_motor.stop()
    r.robot.turn(25)
    r.robot.straight(500)
    r.robot.turn(-60)
    r.robot.straight(60)
    # the robot drives into the inivation project module circle
    r.left_attachment_motor.run(200)
    r.right_attachment_motor.run(200)
    # the robot lets go of the inivation project module into the circle
    wait(500)
    r.right_attachment_motor.stop()
    r.left_attachment_motor.stop()
    r.robot.straight(225)
    # the robot drives foward and pushes the hand into it's possition ending the run.
    #      _!_
    #   o=(0_0)=0
    #   >--(%)--<
    #     _/ /_
    #   Bussin Bot


