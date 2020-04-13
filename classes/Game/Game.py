from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero


class Game:
    current_board_index = 0
    boards = []
    save_folder_name = None

    def create_new_board(self):
        new_board = GameBoard.Board(30, 30, "@")
        self.boards.append(new_board)

    def next_board(self):
        self.current_board_index += 1
        if len(self.boards) < self.current_board_index:
            self.create_new_board()

    def previous_board(self):
        self.current_board_index -= 1

    def current_board(self):
        return self.boards[self.current_board_index]

    def create_hero(self):
        """
        Create hero, chose class, name etc from user inputs
        :return:[object] hero
        """
        hero = ("Strażnik Torunia", "@", 1, 1)  # mock
        return hero