from classes.Object.Creature.Hero.Hero import *
from classes.Object.Creature.Monster.Monster import *
from classes.Object.Creature.Monster.Monsters import *
from classes.Object.Creature.NPC.NPC import NPC
import os
import json


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
        if filename.startswith("NPC"):
            obj = load_object_from_file(folder_path + "/" + filename, NPC)
            board.npc.append(obj)


def save_objects_from_board(file_path, board):
    for monster in board.monsters:
        save_object_to_file(f'{file_path}MONSTER${monster.__class__.__name__}${monster.id}.txt', monster)
    for npc in board.npc:
        save_object_to_file(f'{file_path}NPC${npc.__class__.__name__}${npc.id}.txt', npc)


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
    return string_to_return[:-1]     # Remove symbol at end

