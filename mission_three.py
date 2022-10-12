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
    #John and Finn mission
    print("Running Mission 3")
    r.ev3.screen.draw_text(30, 60, "Mission 3")
    # making the robot go backwards 
    r.left_drive_motor = Motor(Port.B,positive_direction=Direction.CLOCKWISE)
    r.right_drive_motor = Motor(Port.C,positive_direction=Direction.CLOCKWISE)
    #robot starts against back wall centered on second bold line
    #make sure robot arm is all the way down
    r.left_attachment_motor.run(-200) 
    r.right_attachment_motor.run(200) 
    wait(500)
    r.left_attachment_motor.stop()
    r.right_attachment_motor.stop() 
    r.robot.straight(150)
    r.robot.turn(-45)
    r.robot.straight(370)
    r.robot.turn(45)
    r.robot.straight(240)
    # at the mission model dump energy units 
    r.robot.straight(-270)
    r.robot.turn(-150)
    r.robot.straight(-50)
    #at the yellow oil pump and back up a tiny bit
    r.robot.straight(10)
    i = 0
    while (i < 3):
        r.left_attachment_motor.run(200) 
        r.right_attachment_motor.run(-200) 
        wait(500)
        r.left_attachment_motor.stop()
        r.right_attachment_motor.stop() 
        wait(500)
        i += 1
    r.robot.straight(100)
    r.robot.turn(-70)
    r.robot.straight(500)
    r.ev3.screen.clear()

    r.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
    r.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
