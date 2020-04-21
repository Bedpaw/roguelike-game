from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero
from utils.utils import clear_screen

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 15
BOARD_HEIGHT = 10


def main():
    my_board = GameBoard.Board(BOARD_WIDTH, BOARD_HEIGHT, Hero('Pawel', '@', 0, 0))
    while True:
        my_board.update_board()
        my_board.print_board()
        my_board.get_user_choice()
        my_board.move_monsters()
        clear_screen()
        print(my_board.pos_x)   # up down
        print(my_board.pos_y)   # right left


if __name__ == '__main__':
    main()
