import pyautogui
import time
import util

pyautogui.PAUSE = 0.15
pyautogui.FAILSAFE = True

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
    time.sleep(1)
    moveToAndClick(fishingPos3, False)
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos4, False)
    moveToAndClick(fishingRodPos, True)
    moveToAndClick(fishingPos5, False)
    print("comendo...")
    moveToAndClick(eatPos, True)
    time.sleep(0.5)

def start():
    print("Posicione o mouse onde está sua vara de pescar...")
    time.sleep(0.5)
    fishingRodPos = util.waitGetMouseStopped()

    print("Posicione o mouse na água onde deve pescar...")
    time.sleep(0.5)
    fishingPos1 = util.waitGetMouseStoppedInWater()

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(0.5)
    fishingPos2 = util.waitGetMouseStoppedInWater()

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(0.5)
    fishingPos3 = util.waitGetMouseStoppedInWater()

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(0.5)
    fishingPos4 = util.waitGetMouseStoppedInWater()

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(0.5)
    fishingPos5 = util.waitGetMouseStoppedInWater()

    print("Posicione o mouse onde está sua comida, para comer...")
    time.sleep(0.5)
    eatPos = util.waitGetMouseStopped()

    while True:
        fishing(
            fishingRodPos, 
            fishingPos1, 
            fishingPos2, 
            fishingPos3, 
            fishingPos4,
            fishingPos5,
            eatPos)

start()