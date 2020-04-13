from random import choice
from utils.random_utils import random_true


def run_move_function(move_type):
    """
    Call function, which will return creature position change on map
    :param move_type:[string] move type defined for each creature
    :return: function call, which return [position_change_x, position_change_y]
    """
    move_functions = {
        'MANUAL': manual,  # player choosing move
        'RANDOM_STRAIGHT': random_straight,  # (-1, 0) or (1, 0) or (0, -1), or (0, 1)
        'RANDOM_DIAGONAL': random_diagonal,  # (1, 1) or (-1, -1) or (-1, 1) or (1, -1)
        "STAY": stay,  # (0, 0)
        'RANDOM': random_move,  # STRAIGHT + DIAGONAL + STAY
    }

    return move_functions[move_type]()


def manual(key):
    """
    Return position change despite of key pressed
    :param key:[char]: Move key pressed by player
    :return:[list]: [change_position_x, change_position_y]
    """
    if key == "w":
        return [0, 1]
    if key == "s":
        return [0, -1]
    if key == "a":
        return [-1, 0]
    if key == "d":
        return [1, 0]


def random_straight():
    if random_true(50):
        position_change_x = choice([-1, 1])
        position_change_y = 0
    else:
        position_change_x = 0
        position_change_y = choice([-1, 1])
    return position_change_x, position_change_y


def random_diagonal():
    position_change_x = choice([-1, 1])
    position_change_y = choice([-1, 1])
    return position_change_x, position_change_y


def stay():
    return 0, 0


def random_move():
    position_change_x = choice([-1, 0, 1])
    position_change_y = choice([-1, 0, 1])
    return position_change_x, position_change_y


# print(run_move_function("RANDOM"))


