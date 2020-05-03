from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero
from games_config.board_factory import create_new_board
from utils.data_manager import *
from time import sleep
from macros import BATTLE_MODES


class Game:
    def __init__(self, player_name, game_name, difficulty_level, hero, start_board_index):
        self.hero = hero
        self.current_board_index = start_board_index
        self.game_name = game_name
        self.save_folder_path = f'db/saves/{player_name}/{self.game_name}'
        self.hero_save_path = f'{self.save_folder_path}/hero.txt'
        self.game_config_path = f'{self.save_folder_path}/game_config.txt'
        self.boards_save_path = f'{self.save_folder_path}/BOARDS'
        self.boards = []
        self.turn_counter = 0
        self.difficulty_level = difficulty_level
        self.endgame = False    # to toogle, when hero/final boss dead
        self.board_changed = False
        self.true_player_position = []  # for loading data
        self.battle_mode = BATTLE_MODES.IMMEDIATE_FIGHT

    def next_board(self):
        self.current_board_index += 1
        self.board_changed = True
        self.hero.position_x = 0
        self.hero.position_y = 0
        if len(self.boards) <= self.current_board_index:
            self.boards.append(create_new_board(self, self.current_board_index))

    def previous_board(self):
        self.current_board_index -= 1
        self.hero.position_x = self.current_board().height
        self.hero.position_y = self.current_board().width - 1  # out of range
        self.board_changed = True
        self.current_board().pos_x = self.hero.position_x
        self.current_board().pos_y = self.hero.position_y

    def current_board(self):
        return self.boards[self.current_board_index]

    def save_game(self):
        for i, board in enumerate(self.boards):
            create_new_folder(f'{self.boards_save_path}/BOARD{i}')
            save_objects_from_board(f'{self.boards_save_path}/BOARD{i}/', board)
        save_object_to_file(self.hero_save_path, self.hero)
        write_game_config(self)


