# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

################################
# Define custom_robot Class
################################
class robot_18300:

    def __init__(self):
        '''
        this is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()
            self.left_attachment_motor = Motor(Port.A)
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
            self.right_attachment_motor = Motor(Port.D)
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=88, axle_track=111)
            self.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
            self.left_color_sensor = ColorSensor(Port.S1)
            self.middle_color_sensor = ColorSensor(Port.S2)
            self.right_color_sensor = ColorSensor(Port.S3)
            self.gyro_sensor = GyroSensor(Port.S4)
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.GREEN)
            self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
            wait(1000)
            self.ev3.screen.clear()    
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK WIRING")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            #self.ev3.speaker.say("startup error, check wiring")
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()

        # This sets the minimum drive speed to prevent stalling
        self.min_drive_speed = 60.

        # This sets how quickly the robot speeds up and slows down
        # unit(s) of speed (mm/s) per 1 unit of distance (mm)
        self.drive_acceleration = 1.

        # This sets the minimum tank turn speed to prevent stalling
        self.min_tank_turn_speed = 30.

        # This is the radius of the wheels in cms
        # This is so we can convert distance to wheel rotation(s) or the 
        # other way around
        self.wheel_radius = 4.4

        # half of the distace between the wheels(in cms, obvously)
        # We need this in order to convert from degrees we want to spin the bot
        # to how far those wheels have to move.
        self.axle_track = 5.6

        # this is the gain we use when going straight with the gyro sensor
        self.gyro_gain = 3

################################
# Define functions 
################################

    # Reset The Gyro
    # To Be Worked on

    # Mathemetical Bound Function
    # To Be Worked on

    # Drive Straight With Gyro
    # To Be Worked on
 
    # Gyro Tank Turn
    # To Be Worked on