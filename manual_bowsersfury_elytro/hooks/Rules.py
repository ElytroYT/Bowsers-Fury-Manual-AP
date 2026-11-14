from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

def HasItems(state: CollectionState, player: int, itemlist: list):
    for item in itemlist:
        if state.count(item, player) < 1:
            return False
    return True

def SuperBell(state: CollectionState, player: int):
    """Does the player have Super Bell unlocked and can they actually get one"""
    if state.count("Super Bell", player) >= 1:
        if state.count("Scamper Shores", player) >= 1:
            return True
        if HasItems(state, player, ["Fort Flaptrap", "Bowser Jr. Cursor"]):
            return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area"]) and state.count("Cat Shine", player) >= 5:
            if state.count("Slipskate Slope", player) >= 1:
                return True
            if HasItems(state, player, ["Clawswipe Colosseum"]):
                return "(|Ground Pound| OR (({SuperBell()} OR {LuckyBell()}) AND |Climb (Cat)|) OR ({PropellerBox(Clawswipe Colosseum)} AND |Boost (Propeller Box)|)) and |Carry/Throw| AND |Bowser Jr. Cursor|"
            if HasItems(state, player, ["Crisp Climb Castle", "Bowser Jr. Cursor", "Propeller Box", "Boost (Propeller Box)"]):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area", "Ruins Area"]) and state.count("Cat Shine", player) >= 20:
            if HasItems(state, player, ["Risky Whisker Island", "Bowser Jr. Cursor"]):
                return True
            if HasItems(state, player, ["Roiling Roller Isle", "Bowser Jr. Cursor"]):
                return True
    return False

def LuckyBell(state: CollectionState, player: int):
    """Does the player have Lucky Bell unlocked and can they actually get one"""
    if state.count("Lucky Bell", player) >= 1:
        if HasItems(state, player, ["Scamper Shores", "Propeller Box", "Boost (Propeller Box)"]):
            return True
        if state.count("Pounce Bounce Isle", player) >= 1:
            if state.count("Bowser Jr. Cursor", player) >= 1:
                return True
            if PropellerBox(state, player, "Pounce Bounce Isle") and state.count("Boost (Propeller Box)", player) >= 1:
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area"]) and state.count("Cat Shine", player) >= 5:
            if state.count("Ruins Area", player) >= 1:
                return True
            if state.count("Slipskate Slope", player) >= 1:
                return True
            if HasItems(state, player, ["Crisp Climb Castle", "Propeller Box", "Boost (Propeller Box)"]):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area", "Ruins Area"]) and state.count("Cat Shine", player) >= 20:
            if HasItems("Mount Magmeow", "Risky Whisker Island", "Pipe Path Tower"):
                return True
    return False

def FireFlower(state: CollectionState, player: int):
    """Does the player have Fire Flower unlocked and can they actually get one"""
    if state.count("Fire Flower", player) >= 1:
        if HasItems(state, player, ["Scamper Shores", "Bowser Jr. Cursor"]):
            return True
        if state.count("Fort Flaptrap", player) >= 1:
            return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area"]) and state.count("Cat Shine", player) >= 5:
            if HasItems(state, player, ["Clawswipe Colosseum", "Bowser Jr. Cursor"]):
                return True
            if state.count("Trickity Tower", player) >= 1:
                return True
            if HasItems(state, player, ["Crisp Climb Castle", "Bowser Jr. Cursor"]):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area", "Ruins Area"]) and state.count("Cat Shine", player) >= 20:
            if state.count("Wasteland Area", player) >= 1:
                return True
            if state.count("Pipe Path Tower", player) >= 1:
                return True
    return False

def BoomerangFlower(state: CollectionState, player: int):
    """Does the player have Boomerang Flower unlocked and can they actually get one"""
    if state.count("Boomerang Flower", player) >= 1:
        if state.count("Pounce Bounce Isle", player) >= 1:
            if state.count("Ground Pound", player) >= 1 or ((SuperBell(state, player) or LuckyBell(state, player)) and (state.count("Climb (Cat)", player) >= 1 or state.count("Dive (Cat)", player) >= 1)) or (PropellerBox(state, player, "Pounce Bounce Isle") and state.count("Boost (Propeller Box)", player) >= 1) or (FireFlower(state, player) and state.count("Throw Fireballs (Fire)", player) >= 1) or (state.count("Cat Shine", player) >= 5 and state.count("Giga Bell", player) >= 1 and state.count("Claw (Cat)", player) >= 1 and state.count("Plessie", player) >= 1):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area"]) and state.count("Cat Shine", player) >= 5:
            if HasItems(state, player, ["Ruins Area", "Bowser Jr. Cursor"]):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area", "Ruins Area"]) and state.count("Cat Shine", player) >= 20:
            if HasItems(state, player, ["Wasteland Area", "Bowser Jr. Cursor"]):
                return True
            if HasItems(state, player, ["Mount Magmeow", "Risky Whisker Island", "Pipe Path Tower", "Bowser Jr. Cursor"]):
                return True
    return False

def SuperLeaf(state: CollectionState, player: int):
    """Does the player have Super Leaf unlocked and can they actually get one"""
    if state.count("Super Leaf", player) >= 1:
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area"]) and state.count("Cat Shine", player) >= 5:
            if HasItems(state, player, ["Slipskate Slope", "Bowser Jr. Cursor"]):
                return True
            if HasItems(state, player, ["Trickity Tower", "Bowser Jr. Cursor"]):
                return True
        if HasItems(state, player, ["Giga Bell", "Claw (Cat)", "Lakeside Area", "Ruins Area"]) and state.count("Cat Shine", player) >= 20:
            if HasItems(state, player, ["Wasteland Area", "Bowser Jr. Cursor"]):
                return True
            if state.count("Roiling Roller Isle", player) >= 1:
                return True
            if state.count("Risky Whisky Island", player) >= 1:
                return True
            if HasItems(state, player, ["Pipe Path Tower", "Bowser Jr. Cursor"]):
                return True
    return False

def PropellerBox(state: CollectionState, player: int, area: str):
    """Does the player have Propeller Box unlocked and can they actually get one to the area"""
    if state.count("Propeller Box", player) >= 1:
        if area in ["Scamper Shores", "Fort Flaptrap", "Pounce Bounce Isle", "Lakeside Area"]:
            if state.count("Scamper Shores", player) >= 1:
                return True
            if HasItems(state, player, ["Pounce Bounce Isle", "Ground Pound"]):
                return True
        if area in ["Slipskate Slope", "Clawswipe Colosseum", "Trickity Tower", "Ruins Area"]:
            if HasItems(state, player, ["Slipskate Slope", "Ice Skate"]):
                return True
            if state.count("Crisp Climb Castle", player) >= 1:
                return True
        if area == "Roiling Roller Isle":
            if state.count("Ground Pound", player) >= 1:
                return True
        if area in ["Pipe Path Tower", "Risky Whisker Island", "Mount Magmeow", "Wasteland Area"]:
            if state.count("Pipe Path Tower", player) >= 1:
                return True
    return False

def Plessie(state: CollectionState, player: int):
    return "|Plessie| and |Cat Shine:5| and |Giga Bell| and |Claw (Cat)|"

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
