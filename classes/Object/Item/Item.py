from classes.Object.Object import MyObject
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *


class Item:

    def __init__(self, is_on_board, positionX, positionY, symbol):
        self.is_on_board = is_on_board
        self.positionX = positionX
        self.positionY = positionY
        self.symbol = symbol


    """
    is_on_board = T/F
    positionX
    positionY
    appear_on_board
    take_item
    delete_item
    symbol = *
    """

    def is_on_board