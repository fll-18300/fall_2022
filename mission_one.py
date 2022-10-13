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

    ############################
    # BEGIN: EXAMPLE FROM THE SPRING
    ############################
    # Create and define distance, speed, and turn variables
    # to control how fast the robot moves, how sharp it turns, and how far it will go.
    # Reset the robot distance to zero
    speed = 200
    turn = -10
    distance = 600
    r.robot.reset()

    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (r.robot.distance() <= distance):
        r.robot.drive(speed,turn)
    
    print("The robot has moved " + str(r.robot.distance()) + " mm")

    # r.robot.drive() goes on forever, even after the while loop ends.
    # You need to stop the robot after exiting the while loop
    r.robot.stop()

    ############################
    # END: EXAMPLE FROM THE SPRING
    ############################

    r.left_attachment_motor.run(200) 
    wait(1000)
    r.left_attachment_motor.stop()
    r.robot.straight(-100)
    r.left_attachment_motor.run(-200) 
    wait(250)
    r.left_attachment_motor.stop() 
    r.robot.straight(100)
    r.left_attachment_motor.run(-200) 
    wait(500)
    r.left_attachment_motor.stop()
    r.robot.straight(-600)
    r.ev3.screen.clear()