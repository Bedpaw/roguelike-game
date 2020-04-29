from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import COLOR
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.utils import clear_screen


class Knight(Hero):
    def __init__(self, name="Set_me_name", symbol_on_map="K", position_x=0, position_y=0,
                 strength=20,
                 hp=300,
                 max_hp=300,
                 agility=10,
                 phys_dmg=25,
                 luck = 3,
                 doge_chance = 2,
                 defense = 5,
                 stamina = 15,
                 energy = 10,
                 magic_dmg = 10,
                 mana = 50,
                 max_mana = 50,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Knight',
                    
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility,
                         color_in_battle, move_type, level, exp, exp_to_next_level,phys_dmg,
                         luck,doge_chance,defense,stamina,energy,magic_dmg,mana,max_mana,)
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

    def show_stats_breed(self):
        clear_screen()
        print(f"{' '*5}class: {self.breed} level: {self.level}")
        x = self.stats_info()
        print(x)
        pass

