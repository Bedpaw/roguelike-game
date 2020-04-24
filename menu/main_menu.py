from utils.decorations import cprint
from macros.COLORS import *
from game_engine import game_engine
from utils import data_manager


def run_main_menu(player_name):
    # Logo?
    # clear screen

    cprint(f'Welcome {player_name}!\n', COLOR.YELLOW)
    print("[1] PLAY NEW GAME\n"
          "[2] LOAD GAME\n"
          "[3] ABOUT US\n" #TODO PATI
          "[4] HIGH SCORES\n") # maybe from db some stats, how many monsters, level, name, type of hero

    user_choice = int(input("What do you want to do today?"))

    # if 1 or 2
    # game_engine(user_choice, player_name)


