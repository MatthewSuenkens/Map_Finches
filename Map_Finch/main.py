import easygui as eg
from finch import Finch
import finchconnection
from time import sleep

finch = Finch()

while (1):
    response = eg.buttonbox("Which way would you like to go? You can also change the color of the break!", "Finch controller", ["Up", "Down","Left","Right", "Red", "Green", "Blue"])
    if (response == "Up"):
        finch.wheels(1, 1)
        sleep(0.5)
        finch.wheels(0, 0)
    elif (response == "Down"):
        finch.wheels(-1, -1)
        sleep(0.5)
        finch.wheels(0, 0)
    elif (response == "Right"):
        finch.wheels(1, -1)
        sleep(0.5)
        finch.wheels(0, 0)
    elif (response == "Left"):
       finch.wheels(-1, 1)
       sleep(0.5)
       finch.wheels(0, 0)
    elif (response == "Red"):
        finch.led(255, 0, 0)
    elif (response == "Green"):
        finch.led(0, 255, 0)
    else:
        finch.led(0, 0, 255)
