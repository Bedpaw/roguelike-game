from utils import key_service, validation
from classes.Board import GameBoard

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def main():

    my_board = GameBoard.Board(BOARD_WIDTH, BOARD_HEIGHT, PLAYER_ICON)
    while True:

        my_board.print_board()
        my_board.remove_player_track()
        key_press = key_service.key_pressed()
        validation_move = validation.validate_move_out_of_border(key_press, my_board)
        key_service.key_service_events(key_press, validation_move, my_board, my_board.pos_x, my_board.pos_y) 
        key_service.clear_screen()


if __name__ == '__main__':
    main()

