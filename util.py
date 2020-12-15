import pyautogui
import time
from datetime import datetime
import json
import jsonpickle

CONFIG_FILE_NAME = './config.json'
CONFIG_FISHING_FILE_NAME = './config_fishing.json'

class Position(object):
    def __init__(self, x: int, y: int, color: str):
        self.x  = x
        self.y = y
        self.color = color

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class Config(object):
    def __init__(self, battlePos: Position, foodPos: Position, manaPos: Position, inventoryRingSlot: Position, backpackRingSlot: Position):
        self.battlePos = battlePos
        self.foodPos = foodPos
        self.manaPos = manaPos
        self.inventoryRingSlot = inventoryRingSlot
        self.backpackRingSlot = backpackRingSlot

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class ConfigFishing(object):
    def __init__(self, fishingRodPos: Position, fishingPos1: Position, fishingPos2: Position, eatFoodPos: Position):
        self.fishingRodPos = fishingRodPos
        self.fishingPos1 = fishingPos1
        self.fishingPos2 = fishingPos2
        self.eatFoodPos = eatFoodPos

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class AnomObject(object):
    def __init__(self, **kwargs):
         self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

def rgbToHex(rgb):
    return str('#%02x%02x%02x' % rgb)

def dateTimeStr():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]

def log(msg):
    print(dateTimeStr() + " " + msg)

def waitGetMouseStoppedInWater():
    oldPosition = Position(x=0, y=0, color="")
    newPosition = None
    while newPosition is None:
        print("continue com o mouse parado...")
        oldPosition = newPosition
        pos = pyautogui.position()
        newPosition = Position(x=pos.x, y=pos.y, color=rgbToHex(pyautogui.pixel(pos.x,pos.y)))
        time.sleep(3)

    print("posição identificada!")
    return newPosition


def waitGetMouseStopped():
    oldPosition = Position(x=0, y=0, color="")
    newPosition = None
    while newPosition is None or oldPosition != newPosition:
        print("continue com o mouse parado...")
        oldPosition = newPosition
        pos = pyautogui.position()
        newPosition = Position(x=pos.x, y=pos.y, color=rgbToHex(pyautogui.pixel(pos.x,pos.y)))
        time.sleep(3)

    print("posição identificada!")
    return newPosition

def writeFishingConfigJson(config):
    jsonStr = jsonpickle.encode(config)
    with open(CONFIG_FISHING_FILE_NAME, 'w') as f:
        f.write(jsonStr)

def writeConfigJson(config):
    jsonStr = jsonpickle.encode(config)
    with open(CONFIG_FILE_NAME, 'w') as f:
        f.write(jsonStr)

def loadConfigFromJson():
    jsonStr = open(CONFIG_FILE_NAME).read()
    return jsonpickle.decode(jsonStr)

def loadFishingConfigFromJson():
    jsonStr = open(CONFIG_FISHING_FILE_NAME).read()
    return jsonpickle.decode(jsonStr)   