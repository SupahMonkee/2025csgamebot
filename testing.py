import pyautogui as p
import time as t

while True:
    t.sleep(0.5)
    x = p.locateOnScreen(image ='images/test.png', confidence=0.2)
    try:
        #x = p.pixel(100,100)
        x = p.locateOnScreen(image ='images/google.png', confidence=0.8)
        p.moveTo(x)
        x = p.locateOnScreen(image ='images/win.png', confidence=0.8)
        p.moveTo(x)
    except:
        print('not found')


#IT FINALLY WORKS
# GET STARTED on BOT