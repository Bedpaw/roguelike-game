from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero
from games_config.board_factory import create_new_board
from utils.data_manager import *


class Game:
    def __init__(self, player_name, game_name, difficulty_level, hero, start_board_index):
        self.hero = hero
        self.current_board_index = start_board_index
        self.game_name = game_name
        self.save_folder_path = f'db/saves/{player_name}/{self.game_name}'
        self.hero_save_path = f'{self.save_folder_path}/hero.txt'
        self.boards_save_path = f'{self.save_folder_path}/BOARDS'
        self.boards = []
        self.turn_counter = 0
        self.difficulty_level = difficulty_level
        self.endgame = False    # to toogle, when hero/final boss dead
        self.counter = 1  # test only
        self.board_changed = False
    last_map_pos = []

    # def create_new_board(self):
    #     new_board = GameBoard.Board(self, 15 + self.counter, 8 + self.counter, self.hero)
    #     self.boards.append(new_board)
    #     self.counter += 5   # test

    def next_board(self):
        self.current_board_index += 1
        self.last_map_pos = [self.hero.position_x, self.hero.position_y]
        self.board_changed = True
        self.hero.position_x = 0
        self.hero.position_y = 0
        if len(self.boards) <= self.current_board_index:
            self.boards.append(create_new_board(self, self.current_board_index))


    def previous_board(self):
        self.hero.position_x = self.last_map_pos[0]
        self.hero.position_y = self.last_map_pos[1]-1
        self.board_changed = True
        self.current_board_index -= 1

    def current_board(self):
        return self.boards[self.current_board_index]

