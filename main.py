import util
import engine
import ui
import game_board
import time


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 10
BOARD_HEIGHT = 10


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():

    # print(f'''
    #          1. New game
    #          2. Intro
    #          3. Hall of flame
    #          4. About\n''') 
    # For now just prototype of menu
    my_board = game_board.Board(BOARD_WIDTH, BOARD_HEIGHT, PLAYER_ICON)
    my_board.create_board()
    print(my_board.game_board_in_class)
    x = 0
    y = 0
    # player_position
    # sign_on_map = 'X'
    # my_board.update_board(x, y)
    # my_board.print_board()

    while True:
        # if my_board.pos_x is None:
        #     sign_on_map = ''
        my_board.print_board()
        my_board.remove_player_track()
        if util.key_pressed() == 'p':
            exit(0)
        if util.key_pressed() == 'w':
            x -= 1
            my_board.update_board(x, y)
            print('UPUPUP')
            
        elif util.key_pressed() == 's':
            x += 1
            my_board.update_board(x, y)
            print('DOWN')
            
        elif util.key_pressed() == 'a':
            y -= 1
            my_board.update_board(x, y)
            print('LEFT')
            
        elif util.key_pressed() == 'd':
            y += 1
            my_board.update_board(x, y)
            print('RIGHT')

        
        util.clear_screen()






    # print(my_board.game_board_in_class)


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
