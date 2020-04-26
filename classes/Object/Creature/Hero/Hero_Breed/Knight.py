from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import COLOR
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.validation import int_input

class Knight(Hero):
    def __init__(self, name="Set_me_name", symbol_on_map="K", position_x=0, position_y=0,
                 strength=30,
                 hp=400,
                 max_hp=400,
                 agility=10,
                 luck=5,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Knight'
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility, luck,
                         color_in_battle, move_type, level, exp, exp_to_next_level)
        self.breed = breed


    # level up attributes


    skill_improv = {
            "1": {
                "skill": "strength",
                "amount": 10,
            },
            "2": {
                "skill": "hp",
                "skill2": "max_hp",
                "amount": 50,
            },
            "3": {
                "skill": "agility",
                "amount": 5,
            },
            "4": {
                "skill": "luck",
                "amount": 5,
            }
        }



