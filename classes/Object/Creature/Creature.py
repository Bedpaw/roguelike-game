from classes.Object.Object import MyObject
from utils.random_utils import random_move, random_true
from utils.Colored import Colored


class Creature(MyObject):
    """

    """

    hp = 100
    max_hp = 100
    strength = 5  # Damage points by attack
    agility = 10  # Chances to dodge [ % ]
    luck = 10  # Chances to critical strike [ % ]
    color_in_battle = "black"

    def colon_name(self):
        return self.name + ": "

    def move(self):
        end_move = False
        while not end_move:
            position_change = random_move(1, False)
            position = [self.position_x - position_change[0], self.position_y - position_change[1]]
            if self.Board.check_move_possibility(self, position):
                self.position_x = position[0]
                self.position_y = position[1]
                end_move = True

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            self.delete_from_board()
            return False

    def print_hp(self):
        if self.hp < 0:
            self.hp = 0

        hp_left_prec = (self.hp / self.max_hp) * 100
        hp_message = self.colon_name() + str(self.hp) + "/" + str(self.max_hp) + " HP " + "\n"

        if hp_left_prec >= 60:
            Colored(hp_message).cprint(color="green")
        elif hp_left_prec <= 30:
            Colored(hp_message).cprint(color="red", attrs="B")
        else:
            Colored(hp_message).cprint(color="yellow")

    def attack(self, target):
        Colored(self.name + " attack!").cprint(color=self.color_in_battle)
        # check for dodge
        if random_true(target.agility):
            Colored(target.name + " dodged " + self.name + "'s attack!").cprint(color=target.color_in_battle)

        # check for critical attack
        elif random_true(self.luck):
            Colored(self.name + " critical strike with double damage!").cprint(color="red", attrs="U")
            target.hp -= 2 * self.strength

        # normal attack
        else:
            target.hp -= self.strength

        pass

