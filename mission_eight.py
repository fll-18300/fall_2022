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
    r.robot.turn(-15)
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
    wait(500)
    r.robot.straight(205)
    r.right_attachment_motor.run(-200)
    wait(500)
    r.right_attachment_motor.stop()
    r.robot.straight(-100)
    #The robot turns toward the solar farm
    r.robot.turn(150)
    r.robot.straight(-280)
    r.robot.turn(-20)
    r.robot.straight(-230)
    #r.robot.turn(-160)
    r.robot.stop()
    r.gyro_tank_turn(300, -140)
    r.robot.straight(-340)
    # the robot drives foward and pushes the hand into it's possition ending the run.
    #      _!_
    #   o=(0_0)=0
    #   >--(%)--<
    #     _| |_
    #   Bussin Bot


