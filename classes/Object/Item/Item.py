from classes.Object.Object import MyObject
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *


class Item:

    def __init__(self, name, is_on_board, positionX, positionY, symbol, exp, hp, strength):
        self.name = name
        self.is_on_board = is_on_board
        self.positionX = positionX
        self.positionY = positionY
        self.symbol = symbol
        self.exp = exp
        self.hp = hp
        self.strength = strength


    """
    is_on_board = T/F
    positionX
    positionY
    appear_on_board
    take_item
    delete_item
    symbol = *
    exp = how much exp is giving to hero
    hp = how much hp is giving
    strength = how much strength is giving
    """

    def is_on_board(self):

