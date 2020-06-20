import pyautogui
import time
from util import log, AnomObject, rgbToHex, loadConfigFromJson

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = False

CONFIG = loadConfigFromJson()

#### START EXTRA CONFIG
extraConfig = AnomObject(
    logoutWhenNotAlone = True, 
    runeMagicSpell = 'adori gran',
    mlTrainingSpell = 'exura',
    faceDirectionKey = 'a', #a,s,w,d
    loopsToHarlemShake = 9999999999999,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 100,
    _currentLoopsWithoutEatFood = 0,
    loopsToPullRing = 500,
    _currentLoopsWithoutPullRing = 0,
    maxRunes = 350,
    _currentRuneCount = 0,
    makeFood = False,
    runesToExevoPan = 3,
    _currentRuneToExevoPanCount = 0,
)
#### END EXTRA CONFIG

def isAlone():
    battleColor = rgbToHex(pyautogui.pixel(CONFIG.battlePos.x,CONFIG.battlePos.y))
    alone = battleColor == CONFIG.battlePos.color
    return alone

def hasMana():
    manaColor = rgbToHex(pyautogui.pixel(CONFIG.manaPos.x,CONFIG.manaPos.y))
    mana = manaColor == CONFIG.manaPos.color
    return mana

def doLogout():
    pyautogui.press('printscreen')
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')

def makeRune():
    if extraConfig._currentRuneCount < extraConfig.maxRunes:
        extraConfig._currentRuneCount += 1
        log("fazendo runa")
        pyautogui.press("enter")
        pyautogui.typewrite(extraConfig.runeMagicSpell)
        pyautogui.press("enter")
    else:
        log("treinando ml")
        pyautogui.press("enter")
        pyautogui.typewrite(extraConfig.mlTrainingSpell)
        pyautogui.press("enter")


def doHarlemShake():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.press('d')
    pyautogui.press(extraConfig.faceDirectionKey)
    pyautogui.keyUp('ctrl')

def eatFood():
    pyautogui.rightClick(CONFIG.foodPos.x, CONFIG.foodPos.y)

def checkIsAlone():
    if not isAlone():
        log("não está mais sozinho!!!")
        if extraConfig.logoutWhenNotAlone:
            print("fazendo logout!")
            doLogout()
            exit()

def shouldDoExevoPan():
    if extraConfig.makeFood:
        extraConfig._currentRuneToExevoPanCount += 1
        return extraConfig._currentRuneToExevoPanCount >= extraConfig.runesToExevoPan
    else:
        return False

def doExevoPan():
    log("fazendo food")
    pyautogui.press("enter")
    pyautogui.typewrite("exevo pan")
    pyautogui.press("enter")
    extraConfig._currentRuneToExevoPanCount = 0

def checkMakeRune():
    if hasMana():
        if shouldDoExevoPan():
            doExevoPan()
        else:
            makeRune()

def checkHarlemShake():
    extraConfig._currentLoopsWithoutHarlemShake += 1
    if extraConfig._currentLoopsWithoutHarlemShake >= extraConfig.loopsToHarlemShake:
        doHarlemShake()
        extraConfig._currentLoopsWithoutHarlemShake = 0

def checkEatFood():
    extraConfig._currentLoopsWithoutEatFood += 1
    if extraConfig._currentLoopsWithoutEatFood >= extraConfig.loopsToEatFood:
        eatFood()
        extraConfig._currentLoopsWithoutEatFood = 0

def checkLifeRingPull():
    extraConfig._currentLoopsWithoutPullRing += 1
    if extraConfig._currentLoopsWithoutPullRing >= extraConfig.loopsToPullRing:
        pullRing()
        extraConfig._currentLoopsWithoutPullRing = 0

def pullRing():        
    pyautogui.moveTo(CONFIG.backpackRingSlot.x, CONFIG.backpackRingSlot.y)
    pyautogui.mouseDown(button='left', x=CONFIG.backpackRingSlot.x, y=CONFIG.backpackRingSlot.y)
    pyautogui.moveTo(CONFIG.inventoryRingSlot.x, CONFIG.inventoryRingSlot.y)
    pyautogui.mouseUp(button='left', x=CONFIG.inventoryRingSlot.x, y=CONFIG.inventoryRingSlot.y)

def start():
    log("config carregada: " + str(CONFIG))
    time.sleep(3)
    log("jogando! extraConfig: " + str(extraConfig))
    
    while True:
        checkIsAlone()
        checkMakeRune()
        checkIsAlone()
        checkHarlemShake()
        checkIsAlone()
        checkEatFood()
        checkIsAlone()
        checkLifeRingPull()
        checkIsAlone()

start()