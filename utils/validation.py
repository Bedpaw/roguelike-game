import time


def validate_move_out_of_border(key_press, my_board):
    
    if key_press == 'w':
        if my_board.pos_x == 1 or (my_board.pos_y == 0 and my_board.pos_x == 0):
            print('You are not allowed to use W key.')
            time.sleep(0.8)
            return False
        else:
            return True

    if key_press == 's':
        if my_board.pos_x == my_board.height or (my_board.pos_y == my_board.width and my_board.pos_x == my_board.height):
            print('You are not allowed to use S key.')
            time.sleep(0.8)
            return False
        else:
            return True

    if key_press == 'a':
        for item in my_board.game_board_in_class[1:-1]:
            if my_board.pos_y == 0:
                print('You are not allowed to use A key.')
                time.sleep(0.8)
                return False
        return True

    if key_press == 'd':
        if my_board.pos_x == 0 and my_board.pos_y == 0:
            return True
        
        if my_board.pos_y == my_board.width-1 and my_board.pos_x == my_board.height:
            return True

        for item in my_board.game_board_in_class[1:-1]:
            if my_board.pos_y == my_board.width-1:
                print('You are not allowed to use D key.')
                time.sleep(0.8)
                return False
        return True
