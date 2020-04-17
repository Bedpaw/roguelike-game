from utils import key_service, validation
from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 10
BOARD_HEIGHT = 5


def main():

    my_board = GameBoard.Board(BOARD_WIDTH, BOARD_HEIGHT, Hero('Pawel', '@', 0, 0))
    while True:
        my_board.make_empty_list()
        my_board.print_board()
        my_board.get_user_choice()
        my_board.move_monsters()
        key_service.clear_screen()
        my_board.update_board()


if __name__ == '__main__':
    main()

