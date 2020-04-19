from utils import key_service, validation
from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero
from utils.utils import clear_screen

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 15
BOARD_HEIGHT = 8


def main():

    my_board = GameBoard.Board(BOARD_WIDTH, BOARD_HEIGHT, Hero('Pawel', '@', 0, 0))
    while True:
        my_board.update_board()
        my_board.print_board()
        my_board.get_user_choice()
        my_board.move_monsters()
        clear_screen()
    



if __name__ == '__main__':
    main()

