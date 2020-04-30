from classes.Object.Creature.Monster.Monster import Monster
from macros import MOVES_TYPES
from macros.COLORS import *
from classes.Object.Item.Item import Item


class Troll(Monster):
    strength = 40
    max_hp = 200
    hp = 200
    move_type = MOVES_TYPES.RANDOM_DIAGONAL
    exp = 100
    loot = {
        "coins": 150,

    }
    field_color = BG_COLOR.BLUE
    field_move_possible = True


class Arnold(Monster):
    move_type = MOVES_TYPES.RANDOM
    strength = 40
    exp = 1000
    agility = 50
    luck = 100
    field_color = BG_COLOR.BLUE
    field_move_possible = True

    on_die_message = "I will be back"


