from menu.log_in import log_in
from menu.main_menu import run_main_menu
from utils.utils import clear_screen
from macros.COLORS import *


def main():
    clear_screen()
    cprint("WELCOME IN ANGRY TROLLS!\n", COLOR.BLUE)
    # player_name = log_in()
    # run_main_menu(player_name)
    run_main_menu("PATI")


if __name__ == '__main__':
    main()
