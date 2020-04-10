import util
import engine
import ui
import game_board
import time


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def validate_move_out_of_border(key_press, my_board):
    
    if key_press == 'w':
        if my_board.pos_x == 1 or (my_board.pos_y == 0 and my_board.pos_x == 0):
            print('You are not allowed to use W key.')
            return False
        else:
            return True

    if key_press == 's':
        if my_board.pos_x == my_board.height or (my_board.pos_y == my_board.width and my_board.pos_x == my_board.height):
            print('You are not allowed to use S key.')
            return False
        else:
            return True

    if key_press == 'a':        
        for item in my_board.game_board_in_class[1:-1]:
            if my_board.pos_y == 0:
                print('You are not allowed to use A key.')
                return False
        return True

    if key_press == 'd':
        if my_board.pos_x == 0 and my_board.pos_y == 0:
            return True
        if my_board.pos_x == my_board.width-1 and my_board.pos_y == my_board.height:
            return True
        for item in my_board.game_board_in_class[1:-1]:
            if my_board.pos_y == my_board.height:
                print('You are not allowed to use D key.')
                return False
        return True


def main():

    my_board = game_board.Board(BOARD_WIDTH, BOARD_HEIGHT, PLAYER_ICON)
    x = my_board.pos_x
    y = my_board.pos_y
    while True:

        my_board.print_board()
        my_board.remove_player_track()
        key_press = util.key_pressed()
        validation_move = validate_move_out_of_border(key_press, my_board)

        if validation_move is False:
            my_board.update_board(x, y)
        else:
            if key_press == 'p':
                exit(0)
            elif key_press == 'w':
                x -= 1
                my_board.update_board(x, y)
                
            elif key_press == 's':
                x += 1
                my_board.update_board(x, y)
                
            elif key_press == 'a':
                y -= 1
                my_board.update_board(x, y)
                
            elif key_press == 'd':
                if x == 0 and y == 0:
                    x += 1
                    my_board.update_board(x, y)
                elif x == my_board.width-1 and y == my_board.height:
                    x = len(my_board.game_board_in_class)-1
                    y = 0
                    my_board.update_board(x, y)
                else:
                    y += 1
                    my_board.update_board(x, y)

        time.sleep(0.3) 
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

