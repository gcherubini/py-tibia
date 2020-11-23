import pyautogui
import time
import util
from util import loadFishingConfigFromJson

pyautogui.PAUSE = 0.11
pyautogui.FAILSAFE = True

CONFIG = loadFishingConfigFromJson()

def moveToAndClick(pos, rightClick):
    pyautogui.moveTo(pos.x, pos.y)

    if rightClick is True:
        pyautogui.rightClick(pos.x, pos.y)
    else:
        pyautogui.leftClick(pos.x, pos.y)

def fishing(fishingRodPos, fishingPos1, fishingPos2, fishingPos3, fishingPos4, fishingPos5, eatPos):
    print("pescando...")
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos1, False)
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos2, False)
    moveToAndClick(fishingRodPos, True)
    time.sleep(0.5)
    moveToAndClick(fishingPos3, False)
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos4, False)
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos5, False)
    print("comendo...")
    moveToAndClick(eatPos, True)
    time.sleep(1)

def start():
    while True:
        fishing(
            CONFIG.fishingRodPos, 
            CONFIG.fishingPos1, 
            CONFIG.fishingPos2, 
            CONFIG.fishingPos3, 
            CONFIG.fishingPos4,
            CONFIG.fishingPos5,
            CONFIG.eatFoodPos)

start()