from classes.Object.Object import MyObject
from utils.random_utils import random_true
from utils.decorations import cprint
from events import Move
from macros import MOVES_TYPES
from macros.COLORS import *
from classes.Object.Creature.Hero import Hero


class Creature(MyObject):
    def __init__(self, name="Set_me_name", symbol_on_map="M", position_x=-1, position_y=-1,
                 strength=5, hp=100, max_hp=100, agility=10, luck=10,
                 color_in_battle=COLOR.RED,
                 move_type=MOVES_TYPES.RANDOM, defense = 1):

        super().__init__(name, symbol_on_map, position_x, position_y)
        self.strength = strength
        self.hp = hp
        self.max_hp = max_hp
        self.agility = agility
        self.luck = luck
        self.move_type = move_type
        self.color_in_battle = color_in_battle
        self.defense = defense
    field_move_possible = True

    def move(self, params=None):
        """
        Make creature move, comments below
        :params:any: params for move function
        :return: pass
        """

        # Generate move vector -> example [0, 1]
        position_change_x, position_change_y = Move.run_move_function(self.move_type, params)

        # Calculate where would be creature after move
        position_to_check_x = self.position_x + position_change_x
        position_to_check_y = self.position_y + position_change_y

        return position_to_check_x, position_to_check_y

    def is_alive(self):
        """
        Check if creature is alive.
        Mark to remove from board if is not.
        :return:[bool]: True if alive, False if dead
        """
        if self.hp > 0:
            return True
        else:
            self.delete_from_board()    # :TODO delete?
            if isinstance(self, Hero.Hero): # TODO fix imports
                self.game.endgame = True
            return False

    def print_hp(self):

        hp_left_prec = (self.hp / self.max_hp) * 100
        hp_message = f'{self.name}: {self.hp}/{self.max_hp} HP'

        if hp_left_prec >= 60:
            cprint(hp_message, COLOR.GREEN)
        elif 30 >= hp_left_prec > 0:
            cprint(hp_message, COLOR.RED, STYLES.BOLD)
        elif self.hp <= 0:
            null_hp_message = f'{self.name}: 0/{self.max_hp} HP'
            cprint(null_hp_message, COLOR.YELLOW)

    def attack(self, target, dmg):
        cprint(f'{self.name} attack!', self.color_in_battle)

        # Check for dodge
        if random_true(target.agility):
            cprint(f'{target.name} dodged {self.name}\'s attack!', target.color_in_battle)

        # Check for critical attack
        elif random_true(self.luck):
            cprint(f'{self.name} critical strike with double damage!', COLOR.RED, STYLES.BOLD)
            if dmg >= target.defense:
                target.hp -= 2 * (dmg - target.defense)
            else:
                target.hp -= 5

        # Normal attack
        else:
            if dmg >= target.defense:
                target.hp -= (dmg - target.defense)
            else:
                target.hp -= 5
        pass
