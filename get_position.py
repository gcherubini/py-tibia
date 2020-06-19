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
    print("Posicione o mouse onde APARECERÁ o player na battle..." )
    time.sleep(1)
    battlePos = util.waitGetMouseStopped()
    time.sleep(0.5)

    print("Posicione o mouse no slot de comer food..." )
    time.sleep(1)
    foodPos = util.waitGetMouseStopped()
    time.sleep(0.5)

    print("Posicione o mouse onde tem mana (AZUL) para fazer a runa..." )
    time.sleep(1)
    manaPos = util.waitGetMouseStopped()
    time.sleep(0.5)

    print("Posicione o mouse no slot de ring do inventário..." )
    time.sleep(1)
    inventoryRingSlot = util.waitGetMouseStopped()
    time.sleep(0.5)

    print("Posicione o mouse no primeiro slot de life ring da sua bp..." )
    time.sleep(1)
    backpackRingSlot = util.waitGetMouseStopped()
    time.sleep(0.5)

    configObject = util.Config(
        battlePos = battlePos,
        foodPos = foodPos,
        manaPos = manaPos,
        inventoryRingSlot = inventoryRingSlot,
        backpackRingSlot = backpackRingSlot
    )
    util.writeConfigJson(configObject)
    savedConfig = util.loadConfigFromJson()

    print ("saved config: " + str(savedConfig))

start()