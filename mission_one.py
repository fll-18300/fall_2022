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
    #r.robot.turn(90)
    #r.ev3.speaker.say("Running Mission 1")
    print("Initial gyro angle = " + str(r.gyro_sensor.angle()))
    r.drive_straight(500,1500,use_gyro=True,speed_ramp=True)
    wait(100)
    print("End of first leg (Exp 0) = " + str(r.gyro_sensor.angle()))
    r.gyro_tank_turn(300,180)
    wait(100)
    print("After Turn (Exp 180) = " + str(r.gyro_sensor.angle()))
    r.drive_straight(500,1500,use_gyro=True,speed_ramp=True)
    wait(100)
    print("End of Second leg (Exp 180) = " + str(r.gyro_sensor.angle()))
    r.gyro_tank_turn(300,-180)
    wait(100)
    print("End (Exp 0) = " + str(r.gyro_sensor.angle()))
    wait(5000)