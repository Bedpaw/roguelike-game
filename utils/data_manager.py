from utils.validation import int_input
import os


def get_game_name(player_name):
    games_names = os.listdir(f'db/saves/{player_name}')[::-1]   # reverse, because of os.listdir is strange
    games_as_string = ''
    for i, game_name in enumerate(games_names):
        games_as_string += f'{i + 1}. {game_name[:-7]}\n'  # -7 to remove ".pickle"

    game_choice = int_input(f'Please choose game to load:\n{games_as_string}> ', len(games_names))
    return games_names[game_choice - 1]


def create_new_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
