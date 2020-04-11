import random


def random_true(chance):
    """
    :param chance: [int(1-100)] % chance for True
    :return: [Boolean]
    """
    if chance >= random.randint(1, 100):
        return True
    else:
        return False


def random_move(number_of_tiles, diagonal_forbidden=True):
    """
    :param number_of_tiles: [int] Number of tiles for creature move
    :param diagonal_forbidden: [Boolean] Creature move
    :return: int(-1, 1) or tuple(int(-1, 1), int(-1, 1)) if diagonal_forbidden == False
    """
    coordinate_change_1 = random.randint(-number_of_tiles, number_of_tiles)
    coordinate_change_2 = random.randint(-number_of_tiles, number_of_tiles)
    if diagonal_forbidden:
        return coordinate_change_1
    else:
        return coordinate_change_1, coordinate_change_2





