from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint
from macros import MOVES_TYPES, OBJECT_TYPES


class Hero(Creature):
    level = 1
    exp = 0
    exp_to_next_level = 100
    strength = 50
    hp = 400
    max_hp = 400

    type_of = OBJECT_TYPES.HERO
    move_type = MOVES_TYPES.MANUAL
    color_on_board = COLOR.RED
    color_in_battle = COLOR.GREEN

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
        self.exp_to_next_level = self.exp + self.exp_to_next_level * 1.3
        print(f"You have received {self.level} level!")

        print("Which skills do you want to improve?")
        skill_to_improve = None
        while skill_to_improve not in [1, 2, 3, 4]:
            skill_to_improve = int(input("[1] Strength + 10\n"
                                         "[2] Health + 30\n"
                                         "[3] Agility +5\n"
                                         "[4] Luck +5\n"
                                         "Pick a number: "))
        if skill_to_improve == 1:
            self.strength += 10
        elif skill_to_improve == 2:
            self.hp += 30
            self.max_hp += 30
        elif skill_to_improve == 3:
            self.agility += 5
        elif skill_to_improve == 4:
            self.luck += 5
        pass

    def get_exp(self, exp):
        """
        Add exp and check if lvl up
        :param exp:[int]: exp to add for hero
        :return: pass
        """
        self.exp += exp
        print(f'\nYou have got {exp} exp.')
        if exp >= self.exp_to_next_level:
            self.level_up()
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
