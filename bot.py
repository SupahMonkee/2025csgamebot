import pyautogui as gui
from pyautogui import *
import pydirectinput as di
from pyautogui import *
import time as t
from time import *

def start():
    gui.keyDown('alt')
    gui.press('tab')
    gui.keyUp('alt')
    gui.leftClick(225, 175)
    sleep(0.01)
    gui.leftClick(530,580)
    gui.leftClick(530,580)

def scrolling():
    for i in range(20):
        gui.scroll(-10)

def earlygame():
    gui.click(700,625)
    sleep(0.5)
    gui.moveTo(950,420)
    gui.click()

def bot():
    start()
    sleep(5)
    scrolling()
    earlygame()


bot()