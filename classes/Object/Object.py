from utils.random_utils import random_id


class MyObject:

    def __init__(self, name="Set_me_name", symbol_on_map="M", position_x=-1, position_y=-1):
        self.name = name
        self.symbol_on_map = symbol_on_map
        self.position_x = position_x
        self.position_y = position_y
        self.id = random_id()

    is_on_board = True

    def delete_from_board(self):
        self.is_on_board = False

