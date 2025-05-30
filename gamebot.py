import pyautogui as p
import time as t

def start():
    set = False
    t.sleep(0.1)
    try:
        try:
            x = p.locateOnScreen(image='images/settings.png')
            p.moveTo(x)
            p.click()
            cont = True
        except:
            x = p.locateOnScreen(image='images/settings2.png')
            p.moveTo(x)
            p.click()
        set = True
        if set is True:
            try:
                x = p.locateOnScreen(image='images/screeneffect.png')
                p.moveTo(x)
                p.click()
                screeneff = True
                if screeneff is True:
                    x = p.locateOnScreen(image='images/back.png')
                    p.moveTo(x)
                    p.click()
            except:
                pass
    except:
        set = True
    if set is True:
        try:
            x = p.locateOnScreen(image='images/newgame.png')
            p.moveTo(x)
            p.click()
        except:
            pass
    #if cont is True:  THIS IS FOR IF THERE IS A CONTINUE INSTEAD OF A NEW GAME, NEED TO CLICK YES TO RESTART, BEGIN HERE
        #try:
            #x = p.locateOnScreen()
def tut():
    tutorial = 0
    t.sleep(0.1)
    try:
        x = p.locateOnScreen(image='images/ok.png')
        p.moveTo(x)
        p.click()
        tutorial = 1
    except:
        pass
    if tutorial == 1:
        x = p.locateOnScreen(image='images/info.png')
        p.moveTo(x)
        p.click()

while True:
    start()
    tut()