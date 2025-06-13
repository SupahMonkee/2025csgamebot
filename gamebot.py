import pyautogui as p
import time as t

def start():
    set = False
    t.sleep(0.1)
    try:
        if set == False:
            try:
                x = p.locateOnScreen(image='images/settings.png')
                p.moveTo(x)
                p.click()
                cont = True
                set = True
            except:
                x = p.locateOnScreen(image='images/settings2.png')
                p.moveTo(x)
                p.click()
                set = True
            set = True
        if set == True:
            try:
                x = p.locateOnScreen(image='images/screeneffect.png', confidence=0.7)
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
        try:
            x = p.locateOnScreen(image='images/yestonewgame.png')
            p.moveTo(x)
            p.click()
        except:
            pass

def tut():
    first = False
    tutorial = 0
    t.sleep(0.1)
    try:
        x = p.locateOnScreen(image='images/ok.png')
        p.moveTo(x)
        p.click()
        tutorial = 1
    except:
        tutorial = 1
    if tutorial == 1:
        try:
            x = p.locateOnScreen(image='images/info.png')
            p.moveTo(x)
            p.click()
        except:
            pass
    if first == False:
        try:
            x = p.locateOnScreen(image='images/firstpeon.png')
            p.moveTo(x)
            p.click()
            first = True
        except:
            pass
    if first == True:
        try:
            x = p.locateOnScreen(image='images/close.png')
            p.moveTo(x)
            p.click()
        except:
            pass

def game():
    house = False
    x = 0
    if house == False:
        try:
            x = p.locateOnScreen(image='images/6dollars.png')
            if x != 0:
                x = p.locateOnScreen(image='images/build.png')
                p.moveTo(x)
                p.click()
                t.sleep(0.1)
            x = p.locateOnScreen(image='images/buy5.png')
            p.moveTo(x)
            p.click()
        except:
            pass
    try:
        x = p.locateOnScreen(images='images/5dollars.png')
        p.moveTo(x)
        p.click()
        t.sleep(0.1)
        try:
            x = p.locateOnScreen(image='images/info.png')
            p.moveTo(x)
            p.click()
            t.sleep(0.1)
            try:
                x = p.locateOnScreen(image='images/buy5')
                p.moveTo(x)
                p.click()
            except:
                pass
        except:
            pass
    except:
        pass

while True:
    start()
    tut()
    game()