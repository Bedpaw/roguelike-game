from utils.decorations import cprint
from macros.COLORS import *
from game_engine import load_game
from utils import data_manager
from utils.validation import int_input
from game_engine import game_engine
from mock.new_game_creator_mock import create_new_game_mock
from games_config.new_game_creator import *


def about_us():
    with open("about_us.txt", "r") as f:
        print(f.read())

def welcome_image():
    with open("default.txt", "r") as f:
        for row in f:
            cprint((row[:-1]), BG_COLOR.WHITE, COLOR.DARKGREY, STYLES.BOLD)

def high_scores():
    pass #TODO after W gives me data

def run_main_menu(player_name):

    cprint(f'Welcome {player_name}!\n', COLOR.YELLOW)
    cprint("What do you want to do today?", COLOR.YELLOW)
    user_choice = int_input("[1] PLAY NEW GAME\n"
                       "[2] LOAD GAME\n"
                       "[3] ABOUT US\n"
                       "[4] HIGH SCORES\n",4) # TODO with W /from db some stats, how many monsters, level, name, type of hero

    if user_choice == 1:
        pass
        # game = create_new_game(player_name) # !!! <-- Uncomment for full version
        game = create_new_game_mock()  # !!! <-- Comment for full version
        game_engine(game, player_name)
    elif user_choice == 2:
        game = load_game(player_name)
        game_engine(game, player_name)
    elif user_choice == 3:
        about_us()
    elif user_choice == 4:
        high_scores()





