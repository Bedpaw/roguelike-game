from utils.validation import int_input
import os
import pickle
import os.path
from utils.utils import clear_screen


def get_game_name(player_name):
    games_names = os.listdir(f'db/saves/{player_name}')[::-1]   # reverse, because of os.listdir is strange
    games_as_string = ''
    for i, game_name in enumerate(games_names):
        games_as_string += f'{i + 1}. {game_name[:-7]}\n'  # -7 to remove ".pickle"

    game_choice = int_input(f'Please choose game to load:\n{games_as_string}> ', len(games_names))
    return games_names[game_choice - 1]


def load_game(player_name, resume_game=False):
    if resume_game:
        game_name = "RESUME_GAME.pickle"
    else:
        game_name = get_game_name(player_name)
    path_with_game_data = f'db/saves/{player_name}/{game_name}'
    pickle_in = open(path_with_game_data, "rb")
    game = pickle.load(pickle_in)
    pickle_in.close()
    return game


def create_new_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def load_exist(player_name):
    if os.path.isfile(f'db/saves/{player_name}/RESUME_GAME.pickle'):
        return True
    else:
        clear_screen()
        print("There is no game to load")
        input("Press any key to continue...")
        return False