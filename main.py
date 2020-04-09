import util
import engine
import ui
import game_board

# pip install keyboard

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
    my_board = game_board.Board(BOARD_WIDTH, BOARD_HEIGHT)
    my_board.create_board()
    print(my_board.game_board_in_class)
    x = 2
    y = 3
    sign_on_map = 'M'
    my_board.update_board(x, y, sign_on_map)
    my_board.print_board()
    # print(my_board.game_board_in_class)

    # if keyboard.on_press_key('w', lambda _:print("You pressed p")):
    #     print('Dzialam przysicnalem WWWWWWW')
    # if keyboard.is_pressed('s'):
    #     print('Dzialam przysicnalem ssssssss')
    # if keyboard.is_pressed('a'):
    #     print('Dzialam przysicnalem aaaaaaa')
    # if keyboard.is_pressed('d'):
    #     print('Dzialam przysicnalem ddddddd')
    # player = create_player()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

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
