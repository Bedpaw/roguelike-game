from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.key_service import *
from utils.validation import int_input
import time

class Hero(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="@", position_x=-1, position_y=-1,

                 strength=0,
                 hp=0,
                 max_hp=0,
                 agility=0,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=0,
                 exp=0,
                 exp_to_next_level=0,
                 phys_dmg=0,
                 luck=0,
                 doge_chance=0,
                 defense=0,
                 stamina=0,
                 energy=0,
                 magic_dmg=0,
                 mana=0,
                 max_mana=0,
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility)
        self.color_in_battle = color_in_battle
        self.move_type = move_type
        self.level = level
        self.points_for_level = 0
        self.exp = exp
        self.exp_to_next_level = exp_to_next_level
        self.phys_dmg = phys_dmg
        self.luck = luck
        self.doge_chance = doge_chance
        self.defense = defense
        self.stamina = stamina
        self.energy = energy
        self.magic_dmg = magic_dmg
        self.mana = mana
        self.max_mana = max_mana
        self.breed = 'Knight'
        self.current_choice_index = - 1
    field_color = BG_COLOR.RED
    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.CBLACK

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
        self.points_for_level += 5

    def print_add_points(self):
        choice_possiblities = ['strength', 'agility', 'stamina', 'energy']
        for k, v in self.stats_info().items():
            if isinstance(v, list) and k == choice_possiblities[self.current_choice_index]:
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{BG_COLOR.LIGHTGREY}{k} {v[1]}{v[3]}{v[2]}" % (' ' * 8))
            elif isinstance(v, list):
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{k} {v[1]}{v[3]}{v[2]}" % (' ' * 8))
            else:
                print(f"%s   ({k}:{v})" % (' ' * 8))

    def add_statistic(self):
        # regex in future no time, for now is like it is ... :
        # indexes_of_possibilites = [1, 3, 7, 9]
        # display_add_points = [f"{item} [+] | [-]" if i in indexes_of_possibilites
        #                       else f"{item}" for i, item in enumerate(self.stats_info())]
        stats_key_pressed = False
        choice_possiblities = ['strength', 'agility', 'stamina', 'energy']
        skill_impr = {
            1: self.strength,
            2: self.agility,
            3: self.stamina,
            4: self.energy
        }
        S = 115
        W = 119
        ENTER = 13
        while stats_key_pressed is not 'e':
            clear_screen()

            print('Press [w]/[s] to select skill.')

            if stats_key_pressed == 'w':
                self.current_choice_index -= 1
            if stats_key_pressed == 's':
                self.current_choice_index += 1

            if self.current_choice_index >= len(choice_possiblities):
                if ord(stats_key_pressed) == S:
                    self.current_choice_index = 0
                elif ord(stats_key_pressed) == W:
                    self.current_choice_index = 2
            else:
                if self.current_choice_index == len(choice_possiblities) and ord(stats_key_pressed) == S:
                    self.current_choice_index = 0
                if self.current_choice_index < 0:
                    self.current_choice_index = len(choice_possiblities) - abs(self.current_choice_index)

            for k, v in self.stats_info().items():
                if isinstance(v, list) and k == choice_possiblities[self.current_choice_index]:
                    print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{BG_COLOR.LIGHTGREY}{k} {v[1]}{v[3]}{v[2]}" % (' ' * 8))
                elif isinstance(v, list):
                    print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{k} {v[1]}{v[3]}{v[2]}" % (' ' * 8))
                else:
                    print(f"%s   ({k}:{v})" % (' ' * 8))


            stats_key_pressed = key_pressed()
            if ord(stats_key_pressed) == ENTER:
                return True

            # while not labled:
            #     add_rmv = key_pressed()
            #     if add_rmv == '+':
            #         self.points_for_level -= 1
            #     elif add_rmv == '-':
            #         self.points_for_level += 1
            #     else:
            #         labled = False


            #
            # if ord(stats_key_pressed) == ENTER:
            #     return stats_key_pressed
            #     while add_rmv:
            #         add_rmv = key_pressed()
            #         if add_rmv == '+':
            #             self.points_for_level += 1
            #         elif add_rmv == '-':
            #             self.points_for_level -= 1
            #         elif ord(add_rmv) == ENTER:
            #             add_rmv = False
            #
            #     print('Enter dziala')
            #     time.sleep(1)



        # return '\n'.join(display_add_points)


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

    def stats_info(self):
        plus_minus = ' [+]|[-]'
        return{
                "Skill points": self.points_for_level,
                "strength":  [BG_COLOR.RED, self.strength, STYLES.RESET, plus_minus],
                "physical dmg": self.phys_dmg,
                "agility": [BG_COLOR.GREEN, self.agility, STYLES.RESET, plus_minus],
                "crit_chance": self.luck,
                "doge chance": self.doge_chance,
                "defense": self.defense,
                "stamina": [BG_COLOR.ORANGE, self.stamina, STYLES.RESET, plus_minus],
                "hp": self.hp,
                "energy": [BG_COLOR.BLUE, self.energy, STYLES.RESET, plus_minus],
                "magic dmg": self.magic_dmg,
                "max_mana": self.max_mana
                }


    def show_stats_breed(self):
        clear_screen()
        print(f"{' '*5}{self.breed} level: {self.level}")
        statistic = self.stats_info()
        label_len = 16
        for k, v in statistic.items():
            espace = int((label_len - len(k))/2)
            if isinstance(v, list):
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{espace * ' '} {k} {v[1]}{espace * ' '}{v[2]}" % (' ' * 8))
            else:
                print(f"%s   ({k}:{v})" % (' ' * 8))
        pass


