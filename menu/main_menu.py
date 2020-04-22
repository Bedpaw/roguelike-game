from utils.decorations import cprint
from macros.COLORS import *
from game_engine import game_engine


def run_main_menu(player_name):
    # Logo?
    # clear screen
    cprint(f'Welcome {player_name}!\n', COLOR.YELLOW)
    print("[1] PLAY NEW GAME\n"
          "[2] LOAD GAME\n")

    user_choice = int(input("What do you want to do today?"))

    # if 1 or 2
    # game_engine(user_choice, player_name)

