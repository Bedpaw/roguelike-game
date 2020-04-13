from classes.Object.Object import MyObject
from utils.random_utils import random_true
from utils.decorations import cprint
from events import Move
from macros.COLORS import *


class Creature(MyObject):
    hp = 100
    max_hp = 100
    strength = 5  # Damage points by attack
    agility = 10  # Chances to dodge [ % ]
    luck = 10  # Chances to critical strike [ % ]

    color_in_battle = STYLES.RESET
    move_type = "RANDOM_STRAIGHT"

    def move(self):
        """
        Make creature move, comments below
        :return: pass
        """
        # End move == True, when generated position is valid to move
        end_move = False
        while not end_move:
            # Generate creature position change despite of creature move_type
            position_change_x, position_change_y = Move.run_move_function(self.move_type)

            # Calculate where would be creature after move
            position_to_check_x = self.position_x + position_change_x
            position_to_check_y = self.position_y + position_change_y

            # If new position is free -> move there
            if self.Board.check_move_possibility(self, position_to_check_x, position_to_check_y):
                self.position_x = position_to_check_x
                self.position_y = position_to_check_y
                end_move = True
            pass

    def is_alive(self):
        """
        Check if creature is alive.
        Mark to remove from board if is not.
        :return:[bool]: True if alive, False if dead
        """
        if self.hp > 0:
            return True
        else:
            self.delete_from_board()
            return False

    def print_hp(self):
        if self.hp < 0:
            self.hp = 0

        hp_left_prec = (self.hp / self.max_hp) * 100
        hp_message = f'{self.name}: {self.hp}/{self.max_hp} HP\n'

        if hp_left_prec >= 60:
            cprint(hp_message, COLOR.GREEN)
        elif hp_left_prec <= 30:
            cprint(hp_message, COLOR.RED, STYLES.BOLD)
        else:
            cprint(hp_message, COLOR.YELLOW)

    def attack(self, target):
        cprint(f'{self.name} attack!', self.color_in_battle)

        # check for dodge
        if random_true(target.agility):
            cprint(f'{target.name} dodged {self.name}\'s attack!', target.color_in_battle)

        # check for critical attack
        elif random_true(self.luck):
            cprint(f'{self.name} critical strike with double damage!', COLOR.RED, STYLES.BOLD)
            target.hp -= 2 * self.strength

        # normal attack
        else:
            target.hp -= self.strength
        pass
