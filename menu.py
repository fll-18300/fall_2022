from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait
from mission_one import mission_one
from mission_two import mission_two
from mission_three import mission_three
from mission_four import mission_four

# displays which button runs each launch
def displayMENU(r):
    # top left center bottom right
    r.ev3.screen.draw_text(80, 0, "M1")
    r.ev3.screen.draw_text(150, 60, "M2")
    r.ev3.screen.draw_text(80, 100, "M3")
    r.ev3.screen.draw_text(0, 60, "M4")

# the menu fuction allows you to choose what
# launch to do
def menu(r):

    displayMENU(r)

    while True:
        btns = r.ev3.buttons.pressed()
        if len(r.ev3.buttons.pressed()) == 1:        
            btn = btns[0]
            if btn == Button.UP:
                r.ev3.screen.clear()
                mission_one(r)
                wait(3000)
            elif btn == Button.RIGHT:  
                r.ev3.screen.clear()  
                mission_two(r)
            elif btn == Button.DOWN:
                r.ev3.screen.clear()  
                mission_three(r)
            elif btn == Button.LEFT:
                r.ev3.screen.clear()  
                mission_four(r)
            else:
                print("UNDEFINED BUTTON ERROR!")
        displayMENU(r)
