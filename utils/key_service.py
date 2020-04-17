import sys
import os


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


# def key_service_events(key_press, validation_move, my_board, x, y):
#     if validation_move is False:
#         my_board.update_board(x, y)
#     else:
#         if key_press == 'p':
#             exit(0)
#         elif key_press == 'w':
#             x -= 1
#             my_board.update_board(x, y)
            
#         elif key_press == 's':
#             x += 1
#             my_board.update_board(x, y)
            
#         elif key_press == 'a':
#             y -= 1
#             my_board.update_board(x, y)
            
#         elif key_press == 'd':
#             if x == 0 and y == 0:
#                 x += 1
#                 my_board.update_board(x, y)
#             elif x == my_board.height and y == my_board.width-1:
#                 x = len(my_board.game_board_in_class)-1
#                 y = 0
#                 my_board.update_board(x, y)
#             else:
#                 y += 1
#                 my_board.update_board(x, y)


