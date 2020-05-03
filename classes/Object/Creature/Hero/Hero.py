from classes.Object.Creature.Creature import Creature
from classes.Object.Item.Item import Item
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.key_service import *

from utils.validation import int_input
import time
import operator


class Hero(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="@", position_x=-1, position_y=-1,

                 strength=0,
                 hp=200,
                 max_hp=0,
                 agility=0,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=0,
                 exp=0,
                 exp_to_next_level=0,
                 phys_dmg=0,
                 luck=0,
                 dodge_chance=0,
                 defense=0,
                 stamina=0,
                 energy=0,
                 magic_dmg=0,
                 mana=0,
                 max_mana=0,
                 coins=100,
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
        self.dodge_chance = dodge_chance
        self.defense = defense
        self.stamina = stamina
        self.energy = energy
        self.magic_dmg = magic_dmg
        self.mana = mana
        self.max_mana = max_mana
        self.breed = ''
        self.current_choice_index = - 1
        self.quests = []
        self.inventory = { #rzeczy noszone dodaja statsy
            "shield": None,
            "helmet": None,
            "gloves": None,
            "armor": None,
            "belt": None,
            "boots": None
            }
        self.coins = coins
        self.backpack = [Item.healing_potion()] #rzeczy noszone nie dodaja statsow
        self.spells ={}


    field_color = BG_COLOR.RED
    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.CBLACK


    on_fight_message = "Time to stop this creature!"

    def print_hp(self):
        if self.hp < 0:
            self.hp = 0
        if self.mana < 0:
            self.mana = 0

        hp_left_prec = (self.hp / self.max_hp) * 100
        hp_message = f'{self.name}: {self.hp}/{self.max_hp} HP'

        mana_left_prec = (self.mana / self.magic_dmg) * 100
        mana_message = f'{self.name}: {self.mana}/{self.max_mana} MANA\n'

        if hp_left_prec >= 60:
            cprint(hp_message, COLOR.GREEN)
        elif hp_left_prec <= 30:
            cprint(hp_message, COLOR.RED, STYLES.BOLD)
        else:
            cprint(hp_message, COLOR.YELLOW)

        if mana_left_prec >= 60:
            cprint(mana_message, COLOR.GREEN)
        elif hp_left_prec <= 30:
            cprint(mana_message, COLOR.RED, STYLES.BOLD)
        else:
            cprint(mana_message, COLOR.YELLOW)

    def level_up_attributes(self):
        #DON'T TOUCH IT
        pass

    def calculate_extra_attributes(self, skill_choice, stats_ratio, add_rmv):
        operator_choice = {
            '+': operator.add,
            '-': operator.sub
        }
        if skill_choice == 0:
            self.phys_dmg = operator_choice[add_rmv](self.phys_dmg, stats_ratio[skill_choice])
        if skill_choice == 1:
            self.luck = operator_choice[add_rmv](self.luck, stats_ratio[skill_choice][0])
            self.dodge_chance = operator_choice[add_rmv](self.dodge_chance, stats_ratio[skill_choice][1])
            self.defense = operator_choice[add_rmv](self.defense, stats_ratio[skill_choice][2])
        if skill_choice == 2:
            self.hp = operator_choice[add_rmv](self.hp, stats_ratio[skill_choice])
            self.max_hp = operator_choice[add_rmv](self.max_hp, stats_ratio[skill_choice])
        if skill_choice == 3:
            self.magic_dmg += stats_ratio[skill_choice][0]
            self.mana = operator_choice[add_rmv](self.mana, stats_ratio[skill_choice][1])
            self.max_mana = operator_choice[add_rmv](self.max_mana, stats_ratio[skill_choice][1])


    def level_up(self):
        """
        1) Add level
        2) Set new exp_to_next_level
        3) Improve hero skills
        :return: pass
        """
        self.level += 1
        self.level_up_attributes()
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


    def add_rmv_points(self, skill_choice, add_rmv):
        operator_choice = {
            '+': operator.add,
            '-': operator.sub
        }
        if skill_choice == 0:
            self.strength = operator_choice[add_rmv](self.strength, 1)
        elif skill_choice == 1:
            self.agility = operator_choice[add_rmv](self.agility, 1)
        elif skill_choice == 2:
            self.stamina = operator_choice[add_rmv](self.stamina, 1)
        elif skill_choice == 3:
            self.energy = operator_choice[add_rmv](self.energy, 1)


    def add_statistic(self):

        stats_key_pressed = False
        choice_possiblities = ['strength', 'agility', 'stamina', 'energy']

        S = 115
        W = 119
        ENTER = 13

        while stats_key_pressed is not 'm':
            clear_screen()

            print('Select by [w]/[s] and press[enter] to select skill.')
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

            self.print_add_points()

            stats_key_pressed = key_pressed()

            if ord(stats_key_pressed) == ENTER:
                return True, self.current_choice_index
            if stats_key_pressed == 'm':
                return False, self.current_choice_index

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
                "dodge chance": self.dodge_chance,
                "defense": self.defense,
                "stamina": [BG_COLOR.ORANGE, self.stamina, STYLES.RESET, plus_minus],
                "hp": f"{self.hp}/{self.max_hp}",
                "energy": [BG_COLOR.BLUE, self.energy, STYLES.RESET, plus_minus],
                "magic dmg": self.magic_dmg,
                "max_mana": self.max_mana
                }

    def show_stats_with_add_points(self):

        temp_skill_add_points = self.points_for_level
        labled = True
        while labled:
            val = True
            if labled:
                labled, skill_choice = self.add_statistic()

            while val:
                add_rmv = key_pressed()
                if add_rmv == '+':
                    if self.points_for_level < 1:
                        val = False
                    else:
                        self.points_for_level -= 1
                        self.add_rmv_points(skill_choice, add_rmv)
                        self.calculate_extra_attributes(skill_choice, self.stats_ratio, add_rmv)
                elif add_rmv == '-':
                    if self.points_for_level >= temp_skill_add_points:
                        val = False
                    else:
                        self.points_for_level += 1
                        self.add_rmv_points(skill_choice, add_rmv)
                        self.calculate_extra_attributes(skill_choice, self.stats_ratio, add_rmv)
                elif ord(add_rmv) == 13:
                    val = False
                    labled = True
                elif add_rmv == 'm':

                    val = False
                    labled = False

                self.print_add_points()

    def show_stats_breed(self):
        clear_screen()
        print(f"{' ' * 5}{self.breed} level: {self.level}")
        statistic = self.stats_info()
        label_len = 16
        for k, v in statistic.items():
            espace = int((label_len - len(k)) / 2)
            if isinstance(v, list):
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{espace * ' '} {k} {v[1]}{espace * ' '}{v[2]}" % (' ' * 8))
            else:
                print(f"%s   ({k}:{v})" % (' ' * 8))
        pass

    # -------------------------- ITEMS -------------------------------------------
    def put_on_from_backpack(self, item):
        choosed_item = None
        input("Which item you want to put on you?")
        if item in self.backpack:
            for item.item_type in self.inventory:
                pass #dokonczyc

        choosed_item.add_power(self)

#not finished
    def print_inventory(self, item):
        for k, v in self.inventory.items():
            cprint("--------------------------")
            cprint(f"|{k}| {v.name}|", COLOR.CYAN)
            print(self.coins)
            print(self.backpack)

    def is_in_backpack(self, item_name):
        for item in self.backpack:
            if item.name == item_name:
                return True
        return False

    def remove_from_backpack(self, item_name):
        for i, item in enumerate(self.backpack):
            if item.name == item_name:
                del self.backpack[i]


    # -------- QUESTS ------------- #

    def quest_taken_by_name(self, name):
        for quest in self.quests:
            if quest['name'] == name:
                return True
        return False

    def quest_done_by_name(self, name):
        for quest in self.quests:
            if quest['name'] == name:
                if quest['COMPLETED']:
                    return True
        return False

    # def is_in_backpack(self, item):
    #     if item in self.backpack:
    #         return True
    #     else:
    #         return False

    def use_hpotion(self):
        hpotion = Item.healing_potion()
        if self.is_in_backpack(hpotion):
            hpotion.add_power()
            self.remove_from_backpack(hpotion)
        else:
            cprint("You don't have any healing potion in your backpack!", COLOR.RED)

    def use_mana(self):
        mana = Item.mana()
        if self.is_in_backpack(mana):
            mana.add_power()
            self.remove_from_backpack(mana)

        else:
            cprint("You don't have any mana potion in your backpack!", COLOR.RED)

    def add_to_backpack(self, loot, item):
        for k, v in loot.items():
            if k == "coins":
                self.coins += v
            else:
                self.backpack.append(item)


    # def remove_from_backpack(self, item):
    #     if self.is_in_backpack(item):
    #         del item


