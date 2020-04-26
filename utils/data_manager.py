from games_config.board_factory import create_new_board
from classes.Object.Creature.Monster.Monsters import Troll
from classes.Object.Creature.NPC.NPC import NPC
from classes.Object.Creature.Monster.Monster import Monster
from utils.validation import int_input
import os
import json
import shutil


# utils for reading/writing to files


def load_object_from_file(file_path, object_class):
    """
    :param file_path:file with object in JSON format
    :param object_class: type(object) -> his class
    :return:object
    """
    with open(file_path) as f:
        object_dict = json.load(f)
        obj = object_class()
        for k, v in object_dict.items():
            obj.__setattr__(k, v)
        return obj


def save_object_to_file(file_path, obj):
    """
    :param file_path:string: file with object in JSON format
    :param obj:obj: obj to save
    :return: pass
    """
    json_obj = json.dumps(obj.__dict__)
    with open(file_path, 'w+') as f:
        f.write(json_obj)
    pass


def load_objects_to_board(folder_path, board):
    for filename in os.listdir(folder_path):

        if filename.startswith("MONSTER"):
            class_name = get_string_between_symbol("$", filename)
            obj = load_object_from_file(folder_path + "/" + filename, eval(class_name))
            board.monsters.append(obj)

        elif filename.startswith("NPC"):
            class_name = get_string_between_symbol("$", filename)
            obj = load_object_from_file(folder_path + "/" + filename, eval(class_name))
            board.npc.append(obj)


def save_objects_from_board(file_path, board):
    for monster in board.monsters:
        save_object_to_file(f'{file_path}MONSTER${monster.__class__.__name__}${monster.id}.txt', monster)
    for npc in board.npc:
        save_object_to_file(f'{file_path}NPC${npc.__class__.__name__}${npc.id}.txt', npc)


def load_boards_to_game(game):
    board_names_list = os.listdir(game.boards_save_path)
    for i, board_name in enumerate(board_names_list):
        if game.current_board_index == i:
            board = create_new_board(game, board_index=i, loading=True, current_board=True)
        else:
            board = create_new_board(game, board_index=i, loading=True)
        load_objects_to_board(f'{game.boards_save_path}/{board_name}', board)
        game.boards.append(board)


def get_string_between_symbol(symbol, text):
    """
    Example if  text = dasfsaf$MONSTER$csddsadssd
    symbol = $
    return MONSTER
    :param symbol:string:single char
    :param text:string
    :return:string
    """
    take_letter = False
    string_to_return = ""
    for char in text:
        if take_letter:
            string_to_return += char
        if char == symbol:
            take_letter = not take_letter
    return string_to_return[:-1]  # Remove symbol at end

<<<<<<< HEAD
def read_game_config(player_name):
    game_name = get_game_name(player_name)
=======

def read_game_config(player_name, game_name):
>>>>>>> cc6379c54d52eae76acee8db94ab84b940852ccf
    with open(f'db/saves/{player_name}/{game_name}/game_config.txt', 'r') as f:
        list_of_elements = f.readlines()[1].split(', ')
        difficulty_level, board_index, hero_class = list_of_elements
        return float(difficulty_level), int(board_index), hero_class


def write_game_config(game):
    with open(game.game_config_path, 'w+') as f:
        f.write("difficulty_level, current_board_index, hero_class\n"
                f"{game.difficulty_level}, {game.current_board_index}, {game.hero.__class__.__name__}")


def get_game_name(player_name):
    games_names = os.listdir(f'db/saves/{player_name}')[::-1]
    # READY VERSION, COMMENTED
    # games_as_string = ''
    # for i, game_name in enumerate(games_names):
    #     games_as_string += f'{i + 1}. {game_name}\n'
    #
    # game_choice = int_input(f'Please choose game to load:\n{games_as_string}> ', len(games_names))
    # return games_names[game_choice - 1]
    return games_names[0]   # Mock

def create_new_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
