from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint, ctext
from utils.utils import clear_screen
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.validation import int_input


class Hero(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="@", position_x=-1, position_y=-1,
                 strength=50,
                 hp=400,
                 max_hp=400,
                 agility=10,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility)
        self.color_in_battle = color_in_battle
        self.move_type = move_type
        self.level = level
        self.points_for_level = 0
        self.exp = exp
        self.exp_to_next_level = exp_to_next_level

        self.breed = 'Knight'

    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.CBLACK

    inventory = {
        "coins": 100,
    }
    on_fight_message = "Time to stop this creature!"



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
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)

    def special_attack(self, target):
        """
        Instant kill enemy [only for test]
        :param target:[object] enemy to kill
        :return: pass
        """
        target.hp = 0
        cprint(f'{self.name} is stupid cheater...', self.color_in_battle)

    def show_stats(self):
        clear_screen()
        print(self.name)
        print(f"   strength: {self.strength}")
        print("dmg")
        print(f"   agility: {self.strength}")
        print("attack speed")
        print("critical chance")
        print(f"   stamina: {self.strength}")
        print("defense")
        print(f"   energy: {self.strength}")
        print("Magic dmg")


