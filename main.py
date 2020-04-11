import util
import engine
import ui
import validation
import game_board
import time

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 3
BOARD_HEIGHT = 4


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass





def main():

    my_board = game_board.Board(BOARD_WIDTH, BOARD_HEIGHT, PLAYER_ICON)
    while True:

        my_board.print_board()
        my_board.remove_player_track()
        key_press = util.key_pressed()
        validation_move = validation.validate_move_out_of_border(key_press, my_board)
        util.key_service_events(key_press, validation_move, my_board, my_board.pos_x, my_board.pos_y) 
        util.clear_screen()


    # util.clear_screen()
    # is_running = True
    # while is_running:
    #     engine.put_player_on_board(board, player)
    #     ui.display_board(board)

    #     key = util.key_pressed()
    #     if key == 'q':
    #         is_running = False
    #     else:
    #         pass
    #     util.clear_screen()


if __name__ == '__main__':
    main()

