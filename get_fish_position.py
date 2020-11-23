import pyautogui
import time
import util

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def printConfig(configName, pos):
    print(configName + " = AnomObject(")
    print(str(pos).replace(":", "=").replace("'", "").replace("color= ", "color='").replace("}", "'").replace("{", ""))
    print(")")

def start():
    print("Posicione o mouse onde está sua vara de pescar..." )
    time.sleep(1)
    fishingRodPos = util.waitGetMouseStopped()
    time.sleep(0.5)

    print("Posicione o mouse na água em outro lugar onde deve pescar.." )
    time.sleep(1)
    fishingPos1 = util.waitGetMouseStoppedInWater()
    time.sleep(0.5)

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(1)
    fishingPos2 = util.waitGetMouseStoppedInWater()
    time.sleep(0.5)

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(1)
    fishingPos3 = util.waitGetMouseStoppedInWater()
    time.sleep(0.5)

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(1)
    fishingPos4 = util.waitGetMouseStoppedInWater()
    time.sleep(0.5)

    print("Posicione o mouse na água em outro lugar onde deve pescar..." )
    time.sleep(1)
    fishingPos5 = util.waitGetMouseStoppedInWater()
    time.sleep(0.5)

    print("Posicione o mouse onde está sua comida, para comer..." )
    time.sleep(1)
    eatFoodPos = util.waitGetMouseStopped()
    time.sleep(0.5)
    

    configObject = util.ConfigFishing(
        fishingRodPos = fishingRodPos,
        fishingPos1 = fishingPos1,
        fishingPos2 = fishingPos2,
        fishingPos3 = fishingPos3,
        fishingPos4 = fishingPos4,
        fishingPos5 = fishingPos5,
        eatFoodPos = eatFoodPos
    )
    util.writeFishingConfigJson(configObject)
    savedConfig = util.loadConfigFromJson()

    print ("saved config: " + str(savedConfig))

start()