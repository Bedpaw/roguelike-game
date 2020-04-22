import random
import uuid


def random_true(chance):
    """
    :param chance: [int(1-100)] % chance for True
    :return: [Boolean]
    """
    if chance >= random.randint(1, 100):
        return True
    else:
        return False


def random_id():
    return uuid.uuid4().hex
