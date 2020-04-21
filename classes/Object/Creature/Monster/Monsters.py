from classes.Object.Creature.Monster.Monster import Monster
from macros import MOVES_TYPES
from macros.COLORS import *


class Troll(Monster):
    strength = 20
    max_hp = 200
    hp = 200
    move_type = MOVES_TYPES.STAY
    exp = 100
    loot = {
        "coins": 150,
        "troll_machete": 1
    }
    field_color = BG_COLOR.BLUE


class Arnold(Monster):
    strength = 20
    exp = 1000
    agility = 50
    luck = 100
    field_color = BG_COLOR.BLUE

    on_die_message = "I will be back"


