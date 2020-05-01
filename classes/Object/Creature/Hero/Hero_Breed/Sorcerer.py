from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.validation import int_input

from utils.utils import clear_screen

class Sorcerer(Hero):
    def __init__(self, name="Set_me_name", symbol_on_map="S", position_x=0, position_y=0,
                 strength=68,
                 phys_dmg=12,
                 hp=200,
                 max_hp=200,
                 agility=60,
                 luck=3,
                 dodge_chance=2,
                 defense=5,
                 stamina=15,
                 energy=10,
                 magic_dmg=10,
                 mana=100,
                 max_mana=100,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Sorcer',
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility,
                         color_in_battle, move_type, level, exp, exp_to_next_level,phys_dmg,
                         luck,dodge_chance,defense,stamina,energy,magic_dmg,mana,max_mana)
        self.breed = breed

        # level up attributes

        self.stats_ratio = {
            1: 2,
            2: [3, 2, 3],
            3: [20],
            4: [5, 30]
        }
        self.level_up_attributes = {
            self.hp
        }


    # def add_statistic(self):
    #     display_add_points = [f"{item} [+] | [-]" for item in self.stats_info()]
    #     # regex in future not time for now:
    #     indexes_of_possibilites = [1, 3, 7, 9]
    #     return self.stats_info()


