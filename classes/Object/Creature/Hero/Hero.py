from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.validation import int_input


class Hero(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="@", position_x=0, position_y=0,
                 strength=50,
                 hp=400,
                 max_hp=400,
                 agility=10,
                 luck=10,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility, luck)
        self.color_in_battle = color_in_battle
        self.move_type = move_type
        self.level = level
        self.exp = exp
        self.exp_to_next_level = exp_to_next_level

        self.skill_improv = {
                "1": {
                    "skill": "strength",
                    "amount": 10,
                },
                "2": {
                    "skill": "hp",
                    "skill2": "max_hp",
                    "amount": 30,
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
    field_color = BG_COLOR.RED
    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.RED

    inventory = {
        "coins": 100,
    }
    on_fight_message = "Time to stop this creature!"

    def level_up(self):
        """
        1) Add level
        2) Set new exp_to_next_level
        3) Improve hero skills
        :return: pass
        """
        self.level += 1
        self.exp_to_next_level = self.exp + int(self.exp_to_next_level * 1.3)
        cprint(f"You have received {self.level} level!", SUCCESS)

        skill_to_improve = int_input("Which skill do you want to improve?\n"
                                     "[1] Strength + 10\n"
                                     "[2] Health + 30\n"
                                     "[3] Agility + 5\n"
                                     "[4] Luck + 5\n"
                                     "Pick a number: ", 4)

        for k, v in self.skill_improv.items():
            if k == str(skill_to_improve):
                self.__setattr__(v["skill"], v["amount"] + self.__getattribute__(v["skill"]))
                if "skill2" in v:
                    self.__setattr__(v["skill2"], v["amount"] + self.__getattribute__(v["skill2"]))
        pass

    def get_exp(self, exp):
        """
        Add exp and check if lvl up
        :param exp:[int]: exp to add for hero
        :return: pass
        """
        exp_to_next_level = self.exp_to_next_level - self.exp
        if exp >= exp_to_next_level:
            exp -= exp_to_next_level
            self.level_up()
            self.get_exp(exp)
        else:
            self.exp += exp
        pass

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle, end_enter=1)

    def special_attack(self, target):
        """
        Instant kill enemy [only for test]
        :param target:[object] enemy to kill
        :return: pass
        """
        target.hp = 0
        cprint(f'{self.name} is stupid cheater...', self.color_in_battle)

