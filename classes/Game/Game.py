from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero


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

    def create_new_board(self):
        new_board = GameBoard.Board(15 + self.counter, 8 + self.counter, self.hero)
        self.boards.append(new_board)
        self.counter += 5   # test

    def next_board(self):
        self.current_board_index += 1
        if len(self.boards) <= self.current_board_index:
            self.create_new_board()

    def previous_board(self):
        if self.current_board_index > 0:
            self.current_board_index -= 1

    def current_board(self):
        return self.boards[self.current_board_index]

