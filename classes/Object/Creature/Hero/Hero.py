from classes.Object.Creature.Creature import Creature
from classes.Object.Item.Item import Item
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.key_service import *
from utils.utils import clear_screen

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
                 coins=1000,
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
        self.backpack = [Item.healing_potion(200), Item.healing_potion(100),
                         Item.healing_potion(100), Item.mana(100), Item.mana(150), Item.gloves(7), Item.gloves(10)]
        self.spells ={}
        self.special_buff_iter = 0
        self.special_buff_flag = False
        self.special_buff_dmg = 100
        self.game = None  #mock



    field_color = BG_COLOR.RED
    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.BLUE
    on_fight_message = "Time to stop this creature!"

    def add_to_message_box(self, message):
        self.game.current_board().last_move_message.append(message)

    def print_mana(self):

        if self.mana < 0:
            self.mana = 0

        mana_left_prec = (self.mana / self.magic_dmg) * 100
        mana_message = f'{self.name}: {self.mana}/{self.max_mana} MANA\n'

        if mana_left_prec >= 60:
            cprint(mana_message, COLOR.GREEN)
        elif mana_left_prec <= 30:
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
        self.points_for_level += 10


    def print_add_points(self):
        clear_screen()
        choice_possiblities = ['strength', 'agility', 'stamina', 'energy']
        for k, v in self.stats_info().items():
            if isinstance(v, list) and k == choice_possiblities[self.current_choice_index]:
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{BG_COLOR.LIGHTGREY}{k} {int(v[1])}{v[3]}{v[2]}" % (' ' * 8))
            elif isinstance(v, list):
                print(f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{k} {int(v[1])}{v[3]}{v[2]}" % (' ' * 8))
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

        while stats_key_pressed is not 'j':
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

            if stats_key_pressed == 'j':
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

    def special_buff(self, skill_buff, add_sub):
        operator_choice = {
            '+': operator.add,
            '-': operator.sub
        }
        self.defense = operator_choice[add_sub](self.defense, 100)

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
                "magic dmg": int(self.magic_dmg),
                "max_mana": int(self.max_mana)
                }

    def show_stats_with_add_points(self):

        temp_skill_add_points = self.points_for_level
        labled = True
        while labled:
            clear_screen()
            val = True
            if labled:
                labled, skill_choice = self.add_statistic()
                if labled == False:
                    break
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
                elif add_rmv == 'j':
                    val = False
                    labled = False
                else:
                    print('You have select wrong keys possible: j, +, -, enter')
                    time.sleep(2)

                self.print_add_points()

    def show_stats_breed(self):
        clear_screen()
        statistic = self.stats_info()
        label_len = 16
        valid = True

        while valid:
            clear_screen()
            print(f"{' ' * 5}{self.breed} level: {self.level}")
            for k, v in statistic.items():
                espace = int((label_len - len(k)) / 2)
                if isinstance(v, list):
                    print(
                        f"%s{COLOR.CBLACK}{STYLES.BOLD}{v[0]}{espace * ' '} {k} {v[1]}{espace * ' '}{v[2]}" % (' ' * 8))
                else:
                    print(f"%s   ({k}:{v})" % (' ' * 8))

            keyx = key_pressed()
            if keyx == 'j':
                valid = False

            else:
                print("Please eneter [j] to exit stats!")
                time.sleep(1)
                valid = True
        pass


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

    # -------------------------- ITEMS -------------------------------------------
    def add_to_inventory_from_backpack(self, item):
        if self.inventory[item.item_type] is None:
            self.inventory[item.item_type] = item
            self.add_power(item)
            self.remove_from_backpack(item.name)
        else:
            current_item_in_inventory = self.inventory[item.item_type]
            self.backpack.append(current_item_in_inventory)
            self.del_power(current_item_in_inventory)
            self.inventory[item.item_type] = item
            self.add_power(item)

        self.show_stats_with_add_points()


    def put_on_from_backpack(self):
        """choosing by player what to wear"""

        def print_item_type(item_type):
            clear_screen()
            items = []
            counter = 1
            print(f"You have these {item_type} available:\n")
            for i, item in enumerate(self.backpack):
                if item.item_type == item_type:
                    items.append(item)
                    item_param_name, item_param_value = self.find_parameter(item)

                    print(f'[{counter}] {item.name} --> {item_param_name} + {item_param_value}')
                    counter += 1

            if items:
                item_choice = int_input("Choose item index to put on\n"
                                        "Your choice ", len(items))
                return items[item_choice - 1]
            else:
                clear_screen()
                input("You don't have any item that type!\n Press any key to resume game")
                return False

        clear_screen()
        choosed_item = int_input(f"Which item you want to put on you?\n"
                                 "      [1] gloves\n"
                                 "      [2] helmet\n"
                                 "      [3] armor\n"
                                 "      [4] shield\n"
                                 "      [5] belt\n"
                                 "      [6] boots\n"
                                 "Your choice:  ", 6)
        if choosed_item == 1:
            item = print_item_type("gloves")
            if item:
                self.add_to_inventory_from_backpack(item)
        if choosed_item == 2:
            item = print_item_type("helmet")
            if item:
                self.add_to_inventory_from_backpack(item)
        if choosed_item == 3:
            item = print_item_type("armor")
            self.add_to_inventory_from_backpack(item)
        if choosed_item == 4:
            item = print_item_type("shield")
            self.add_to_inventory_from_backpack(item)
        if choosed_item == 5:
            item = print_item_type("belt")
            self.add_to_inventory_from_backpack(item)
        if choosed_item == 6:
            item = print_item_type("boots")
            self.add_to_inventory_from_backpack(item)




        # for item.item_type in self.inventory:
        #     if str(choosed_item) in item.item_type:
        #         self.inventory[str(choosed_item)] = item.name
        #         choosed_item.add_power(self)


    def how_many_items(self, item_name):

        counter = 0
        for item in self.backpack:
            if item.name == item_name:
                counter += 1
        return counter

#--------- PRINTING INVENTORY --------

    def print_inventory(self):

        clear_screen()
        cprint("+---------------------------------------------------------+", COLOR.PINK,  STYLES.BOLD)
        cprint(f"|----------------|| {self.name.upper()}'S INVENTORY ||-----------------|", COLOR.PURPLE, STYLES.BOLD)
        cprint("+---------------------------------------------------------+\n", COLOR.PINK, STYLES.BOLD)
        if all([v is None for k, v in self.inventory.items()]):
            cprint("      You are naked! Go and find something to put on you!", COLOR.YELLOW, STYLES.BOLD)
        else:
            for k, v in self.inventory.items():
                if v is not None:
                    cprint(f"       You are wearing {k} called {v.name}", COLOR.CYAN)
                else:
                    cprint(f"       You are not wearing any {k}", COLOR.CYAN)

        cprint("\n+---------------------------------------------------------+", COLOR.PINK, STYLES.BOLD)
        cprint(f"|---------------|| {self.name.upper()}'S BACKPACK ||-------------------|", COLOR.PURPLE, STYLES.BOLD)
        cprint("+---------------------------------------------------------+", COLOR.PINK, STYLES.BOLD)

        # --- printing coins ----

        if self.coins > 0:
            print(f"       {self.coins} gold coins are ringing in your pocket\n")
        else:
            print("        You are very poor, go and earn some money, lazy b...ear ;)")

        # --- printing any other things in backpack ---
        cprint(f"You have these items in your backpack:\n", COLOR.YELLOW, STYLES.BOLD)
        temp =[]
        for item in self.backpack:
            if item.item_type not in temp:
                temp.append(item.item_type)
                cprint(f"You have {self.how_many_items(item.name)} {item.name} --> {item.item_type}", COLOR.YELLOW)

        choose_option = int_input("\n Do you want to put on you something from backpack?\n [1] YES, please!\n [2] NO, maybe next time\n",
                  2)
        if choose_option == 1:
            self.put_on_from_backpack()
        else:
            pass
        self.game.current_board().print_board()
        # cprint("\n\n If you want to resume game - press w, s, a or d", COLOR.PURPLE)

    def is_in_backpack(self, item_name):

        for item in self.backpack:
            if item.name == item_name:
                return True
        return False

    def remove_from_backpack(self, item_name):

        for i, item in enumerate(self.backpack):
            if item.name == item_name:
                del self.backpack[i]

    def remove_from_backpack_type(self, item_type):

        for i, item in enumerate(self.backpack):
            if item.item_type == item_type:
                del self.backpack[i]

    def is_in_backpack_type(self, item_type):
        """checking if item is in hero backpack"""

        for item in self.backpack:
            if item.item_type == item_type:
                return True
        return False

    def use_hpotion(self, item_type="healing_potion"):
        """using hp potion from backpack"""

        while self.hp > 0 and self.hp < self.max_hp:
            if self.is_in_backpack_type(item_type):
                self.add_power(Item.healing_potion())
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
                self.remove_from_backpack_type(item_type)
            else:
                cprint("You don't have any healing potion in your backpack!", COLOR.RED)
        else:
            self.add_to_message_box("Your HP is FULL!")


    def use_mana(self, item_type="mana"):

        while self.mana > 0 and self.mana < self.max_mana:
            if self.is_in_backpack_type(item_type):
                self.add_power(Item.mana())
                if self.mana > self.max_mana:
                    self.mana = self.max_mana
                self.remove_from_backpack_type(item_type)
            else:
                cprint("You don't have any mana potion in your backpack!", COLOR.RED)
        else:
            self.add_to_message_box("Your mana is FULL!")

    def add_to_backpack(self, loot):
        """ Adding loots from Monsters and NPC to backpack and to inventory hero"""

        for k, v in loot.items():
            if k == "coins":
                self.coins += v
            else:
                if k in self.inventory.keys():
                    if self.inventory[k] is None:
                        self.inventory[k] = v
                        self.add_power(v)
                    else:
                        self.backpack.append(v)
                else:
                    self.backpack.append(v)


    def add_power(self, item):
        self.strength += item.strength
        self.hp += item.hp
        self.max_hp += item.max_hp
        self.agility += item.agility
        self.energy += item.energy
        self.stamina += item.stamina
        self.mana += item.mana


    def find_parameter(self, item):
        params = [item.strength, item.hp, item.max_hp, item.agility, item.energy, item.stamina, item.mana]
        params_name = {
            0: "strength",
            1: "hp",
            2: "max_hp",
            3: "agility",
            4: "energy",
            5: "stamina",
            6: "mana"
        }
        for i, param_value in enumerate(params):
            if param_value != 0:
                return params_name[i], param_value


    def del_power(self, item):
        self.strength -= item.strength
        self.hp -= item.hp
        self.max_hp -= item.max_hp
        self.agility -= item.agility
        self.energy -= item.energy
        self.stamina -= item.stamina
        self.mana -= item.mana

    def print_loot(self, loot):
        cprint("You have found: ", SUCCESS)
        for k, v in loot.items():
            if k == "coins":
                cprint(f'{v} {k}', SUCCESS)
            else:
                cprint(v.name, SUCCESS)
