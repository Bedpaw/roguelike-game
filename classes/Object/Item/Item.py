from classes.Object.Object import MyObject
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *
from random import random


class Item():

    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    """
    take_item
    hp = how much hp is giving
    strength = how much strength is giving
    """


class Treasure(MyObject):

    message_in_field = cprint(f"You have found {MyObject.__name__}")
    is_locked = ""
    positionX = 1
    positionY = 1

    is_on_board = True

    pass
    """
    is_on_board = T/F
    positionX
    positionY
    is_locked
    message
    """
    def which_item_in(self): # losuje item z dostępnych
        pass