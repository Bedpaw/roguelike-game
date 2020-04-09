from classes.Object.Object import MyObject
from utils.random_utils import random_move, random_true


class Creature(MyObject):
    """

    """
    hp = 100
    max_hp = 100
    strength = 5  # Damage points by attack
    agility = 10  # Chances to dodge [ % ]
    luck = 10  # Chances to critical strike [ % ]

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
        if self.hp >= 0:
            return True
        else:
            self.delete_from_board()
            return False

    def attack(self, target):

        # check for dodge
        if random_true(target.agility):
            print(target.name + " dodged " + self.name + "'s attack!")

        # check for critical attack
        elif random_true(self.luck):
            print(self.name + " critical strike with double damage! ")
            target.hp -= 2 * self.strength

        # normal attack
        else:
            print(self.name + " attack!")
            target.hp -= self.strength
        print(target.name + " : " + str(target.hp) + " HP")
        return target.is_alive()

