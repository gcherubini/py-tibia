import pyautogui
import time
import util
import random
from util import loadFishingConfigFromJson
from util import Position

pyautogui.PAUSE = 0.11
pyautogui.FAILSAFE = True

CONFIG = loadFishingConfigFromJson()

def moveToAndClick(pos, rightClick):
    pyautogui.moveTo(pos.x, pos.y)

    if rightClick is True:
        pyautogui.rightClick(pos.x, pos.y)
    else:
        pyautogui.leftClick(pos.x, pos.y)

def fishing(fishingRodPos, fishingPos1, fishingPos2, eatPos):
    print("pescando...")
    
    for i in range(30):
        moveToAndClick(fishingRodPos, True)

        time.sleep(0.3)

        x = random.randint(fishingPos1.x,fishingPos2.x)
        y = random.randint(fishingPos1.y,fishingPos2.y)
        pos = Position(x=x, y=y, color="")

        moveToAndClick(pos, False)

    time.sleep(0.5)

    print("comendo...")
    moveToAndClick(eatPos, True)

def start():
    while True:
        fishing(
            CONFIG.fishingRodPos, 
            CONFIG.fishingPos1, 
            CONFIG.fishingPos2, 
            CONFIG.eatFoodPos)

start()