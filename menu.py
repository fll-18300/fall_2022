from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait
from mission_one import mission_one
from mission_two import mission_two
from mission_three import mission_three
from mission_four import mission_four
from mission_five import mission_five
from mission_six import mission_six
from mission_seven import mission_seven
from mission_eight import mission_eight
# displays which button runs each launch
def displayMENU(r,menu):
    # clear the display
    # top left center bottom right
    if(menu == 1):
        r.ev3.screen.draw_text(80, 0, "M1")
        r.ev3.screen.draw_text(150, 50, "M2")
        r.ev3.screen.draw_text(80, 100, "M3")
        r.ev3.screen.draw_text(0, 50, "M4")
        r.ev3.screen.draw_text(60, 50, "SWAP")
    else:
        r.ev3.screen.draw_text(80, 0, "M5")
        r.ev3.screen.draw_text(150, 50, "M6")
        r.ev3.screen.draw_text(80, 100, "M7")
        r.ev3.screen.draw_text(0, 50, "M8")
        r.ev3.screen.draw_text(60, 50, "SWAP")

# Cleanup after a mission
def cleanup(r):
    # Stop the robot
    r.robot.stop()
    # Clear the display
    r.ev3.screen.clear()
    # Reset the robot
    r.robot.reset()

# the menu fuction allows you to choose what
# launch to do
def menu(r):
    menu = 1
    displayMENU(r,menu)

    while True:
        displayMENU(r,menu)
        btns = r.ev3.buttons.pressed()
        if len(btns) == 1:        
            btn = btns[0]
            if menu == 1:
                if btn == Button.UP:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 1")
                    mission_one(r)
                    cleanup(r)
                elif btn == Button.RIGHT:  
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 2")  
                    mission_two(r)
                    cleanup(r)
                elif btn == Button.DOWN:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 3")  
                    mission_three(r)
                    cleanup(r)
                elif btn == Button.LEFT:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 4")  
                    mission_four(r)
                    cleanup(r)
                elif btn == Button.CENTER:
                    r.ev3.screen.clear()
                    menu = 2  
                    r.ev3.screen.clear()
                    displayMENU(r,menu)
                    r.ev3.light.off()
                    r.ev3.light.on(Color.ORANGE)
                    wait(500)
                else:
                    print("UNDEFINED BUTTON ERROR!")
            else:
                if btn == Button.UP:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 5")
                    mission_five(r)
                    cleanup(r)
                elif btn == Button.RIGHT:  
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 6")  
                    mission_six(r)
                    cleanup(r)
                elif btn == Button.DOWN:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 7")  
                    mission_seven(r)
                    cleanup(r)
                elif btn == Button.LEFT:
                    r.ev3.screen.clear()
                    r.ev3.screen.draw_text(30, 60, "Mission 8")  
                    mission_eight(r)
                    cleanup(r)
                elif btn == Button.CENTER:
                    menu = 1
                    r.ev3.screen.clear()  
                    displayMENU(r,menu)
                    r.ev3.light.off()
                    r.ev3.light.on(Color.GREEN)
                    wait(500)
                else:
                    print("UNDEFINED BUTTON ERROR!")

