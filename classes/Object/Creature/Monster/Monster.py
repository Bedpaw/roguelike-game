from classes.Object.Creature.Creature import Creature
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *


class Monster(Creature):
    type_of = OBJECT_TYPES.MONSTER
    color_on_board = COLOR.RED
    color_in_battle = COLOR.RED
    on_fight_message = "You have no chance with me! "
    on_die_message = "Argghr.."

    exp = 30
    loot = {
        "coins": 10
    }

    def on_defeat(self):
        cprint(f'{self.name} has been defeated!', ERROR)
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)
