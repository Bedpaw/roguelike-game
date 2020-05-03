from menu.log_in import log_in
from menu.main_menu import run_main_menu
from menu.main_menu import welcome_image
from utils.decorations import cprint
from macros.COLORS import *
from game_engine import game_engine
from mock.new_game_creator_mock import create_new_game_mock



def main():
    welcome_image()
    cprint("WELCOME IN ANGRY TROLLS!\n", COLOR.BLUE)
    player_name = log_in()
    run_main_menu(player_name)

    #   MOCK
    # game = create_new_game_mock()
    # game_engine(game, 'PAWEL')

if __name__ == '__main__':
    main()