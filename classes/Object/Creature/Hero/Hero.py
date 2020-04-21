from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.validation import int_input


class Hero(Creature):
<<<<<<< HEAD
    level = 1
    exp = 0
    exp_to_next_level = 100
    strength = 50
    hp = 400
    max_hp = 400
    field_color = COLOR.BLUE

=======
    def __init__(self, name, symbol_on_map, position_x, position_y,
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
>>>>>>> 2b2a61c7ebe4e7b4ee2761e1f5e7afd903a44ecd

    type_of = OBJECT_TYPES.HERO
    color_on_board = COLOR.RED

    inventory = {
        "coins": 100,
    }
    on_fight_message = "Time to stop this creature!"

    def skill_improv(self):
        return {
            "1": {
                "name": "Strength",
                "skill": self.strength,
                "amount": 10,
            },
            "2": {
                "name": "Health",
                "skill": self.hp,
                "skill2": self.max_hp,
                "amount": 30,
            },
            "3": {
                "name": "Agility",
                "skill": self.agility,
                "amount": 5,
            },
            "4": {
                "name": "Luck",
                "skill": self.luck,
                "amount": 5,
            }
        }

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
        print(self.strength)
        for k, v in self.skill_improv().items():
            if k == str(skill_to_improve):
                print(v["skill"])
                v["skill"] += v["amount"]  # TODO: TO NIE DZIAŁA!!
                if "skill2" in v:
                    v["skill2"] += v["amount"]

        if self.exp > self.exp_to_next_level:
            self.level_up()
        pass

    def get_exp(self, exp):
        """
        Add exp and check if lvl up
        :param exp:[int]: exp to add for hero
        :return: pass
        """
        exp_to_next_level = self.exp_to_next_level - self.exp
        if exp > exp_to_next_level:
            exp -= exp_to_next_level
            self.level_up()
            self.get_exp(exp)
        pass

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)

    def special_attack(self, target):
        """
        Instant kill enemy [only for test]
        :param target:[object] enemy to kill
        :return: pass
        """
        target.hp = 0
        cprint(f'{self.name} is stupid cheater...', self.color_in_battle)
