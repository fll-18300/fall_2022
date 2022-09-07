################################
# robot_18300.py
################################

# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait, StopWatch
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

################################
# Define custom_robot Class
################################
class robot_18300:

    def __init__(self):
        
        '''
        This is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"EV3 FAIL")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_attachment_motor = Motor(Port.A)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT A")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_attachment_motor = Motor(Port.D)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT D")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT B")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT C")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_color_sensor = ColorSensor(Port.S1)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 1")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.middle_color_sensor = ColorSensor(Port.S2)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 2")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_color_sensor = ColorSensor(Port.S3)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 3")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.gyro_sensor = GyroSensor(Port.S4)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 4")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=88, axle_track=115)
            self.robot.settings(straight_speed=600, straight_acceleration=350, turn_rate=200, turn_acceleration=123)
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.GREEN)
            self.watch = StopWatch()
            self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
            self.ev3.screen.set_font(Font(size=30, bold=True))
            wait(1000)
            self.ev3.screen.clear()    
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"NOT WIRING")
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
    def calibrate_gyro(self, port_number):
        retry = 1
        while retry == 1:
            print("calibrating the Gyro")
            self.ev3.screen.draw_text(0, 0, "Reset Gyro")
            self.ev3.screen.draw_text(0, 22, "DO NOT MOVE!")
            if port_number == 1:
                analog_sensor = AnalogSensor(Port.S1)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S1)
                wait(1000)
            elif port_number == 2:
                analog_sensor = AnalogSensor(Port.S2)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S2)
                wait(1000)
            elif port_number == 3:
                analog_sensor = AnalogSensor(Port.S3)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S3)
                wait(1000)
            else:
                analog_sensor = AnalogSensor(Port.S4)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S4)
                wait(1000)
            i = 0
            while i <= 10:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 0, "RESET GYRO")
                self.ev3.screen.draw_text(0, 22, "DO NOT MOVE!")
                self.ev3.screen.draw_text(0, 44, "Gyro= " + str(gyro_sensor.angle()))
                wait(100)
                self.ev3.screen.clear()
                i = i + 1
            if gyro_sensor.angle() == 0:
                retry = 0
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 44, "Gyro")
                self.ev3.screen.draw_text(0, 44, "Calibration")
                self.ev3.screen.draw_text(0, 84, "Complete")
                wait(500)
                self.ev3.screen.clear()
    
    # gyro tank turn
    def gyro_tank_turn(self,speed, angle):
        ''' Tank turn using the gyro
            angle positive = clockwise
            angle negative = counter-clockwise
        '''
        min_speed = 50
        #Get the current angle
        starting_angle = self.gyro_sensor.angle()
        target_angle = starting_angle - angle
        # The gyro is mounted upside-down which reverses the gyro measurements 
        if angle >= 0:
        #clockwise
            while self.gyro_sensor.angle() >= target_angle:
                # Ramp the speed based on the perecntage of the turn completed.
                scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                unbound_speed = speed * (1 - scale)
                current_speed = max(unbound_speed, self.min_tank_turn_speed)
                self.left_drive_motor.run(current_speed)
                self.right_drive_motor.run(-current_speed)
        else:
        #counter-clockwise
            while self.gyro_sensor.angle() <= target_angle:
                # Ramp the speed based on the perecntage of the turn completed.
                scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                unbound_speed = speed * (1 - scale)
                current_speed = max(unbound_speed, self.min_tank_turn_speed)
                self.left_drive_motor.run(-current_speed)
                self.right_drive_motor.run(current_speed)
            self.left_drive_motor.brake()
            self.right_drive_motor.brake()    
                

                

