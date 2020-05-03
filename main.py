from menu.log_in import log_in
from menu.main_menu import run_main_menu
from menu.main_menu import welcome_image
from macros.COLORS import *


def main():
    welcome_image()
    # cprint("WELCOME IN ANGRY TROLLS!\n", COLOR.BLUE)
    # player_name = log_in()
    # run_main_menu(player_name)

    # MOCK 2
    run_main_menu("PAWEL")


if __name__ == '__main__':
    main()
