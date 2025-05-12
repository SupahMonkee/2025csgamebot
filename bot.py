import pyautogui as gui
from pyautogui import *
import pydirectinput as di
from pyautogui import *
import time as t
from time import *

def start():
    #switching to game tab
    gui.keyDown('alt')
    gui.press('tab')
    gui.keyUp('alt')

    #start game
    gui.leftClick(225, 175)
    sleep(0.01)

    #checking for new game
    gui.leftClick(530,580)
    gui.leftClick(530,580)
    

def scrolling():
    #tutorial 1/4
    gui.click(900,500)
    sleep(0.1)
    gui.click(900,500)

    #zoom out
    di.keyDown('-')
    sleep(3)
    di.keyUp('-')

def earlygame():
    #info
    gui.click(700,625)
    sleep(0.1)
    gui.click(700,625)

    #buy peon
    sleep(0.5)
    gui.moveTo(950,420)
    gui.click()

    #tutorial 2/4 3/4
    for i in range(3):
        sleep(0.1)
        gui.click(950,500)
    sleep(1)


    #build plot 1
    gui.moveTo(550,610)
    sleep(0.1)
    gui.click(550,610)

    #waiting to buy house  
    sleep(22)

    #buy house in plot 1
    gui.click(700,360)
    sleep(0.1)

    #info booth for peon 2 and 3
    gui.click(700,625)
    sleep(0.1)
    gui.click(700,625)

    #buy peon 2
    sleep(12)
    gui.click(950,420)

    #buy peon 3
    sleep(12)
    gui.click(950,420)
    
    
    

def bot():
    start()
    sleep(5)
    scrolling()
    earlygame()
    exit()


bot()



