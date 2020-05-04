from macros.COLORS import *
from game_engine import game_engine
from mock.new_game_creator_mock import create_new_game_mock
from games_config.new_game_creator import create_new_game
from utils.validation import int_input
from utils.data_manager import load_game


def about_us(player_name):
    with open("menu/about_us.txt", "r") as f:
        print(f.read())
    answer = input("Please press T for back to main menu")
    if answer.upper() == "T":
        run_main_menu(player_name)


def welcome_image():
    with open("menu/welcome_image.txt", "r") as f:
        for row in f:
            cprint((row[:-1]), BG_COLOR.WHITE, COLOR.LIGHTGREEN, STYLES.BOLD)


def high_scores():
    pass  # TODO after W gives me data


def run_main_menu(player_name):
    cprint("CHOOSE ONE OF BELOW OPTIONS\n", COLOR.YELLOW)
    user_choice = int_input("[1] PLAY NEW GAME\n"

                            "[2] RESUME GAME\n"  # TODO only for players who already played once
                            "[3] LOAD GAME\n"    # TODO only for players who already played once
                            "[4] ABOUT US\n"
                            "[5] HIGH SCORES\n"
                            "[6] EXIT\n"
                            "Your choice: ",
                            6)  # TODO with W /from db some stats, how many monsters, level, name, type of hero


    if user_choice == 1:
        game = create_new_game(player_name) # !!! <-- Uncomment for full version
        # game = create_new_game_mock()  # !!! <-- Comment for full version
        game_engine(game)
    elif user_choice == 2:
        game = load_game(player_name, resume_game=True)
        game_engine(game)
    elif user_choice == 3:
        game = load_game(player_name)
        game_engine(game)
    elif user_choice == 4:
        about_us(player_name)
    elif user_choice == 5:
        high_scores()
    elif user_choice == 6:
        exit()
