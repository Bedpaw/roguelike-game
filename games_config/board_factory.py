from classes.Board.GameBoard import Board
from classes.Board.Fields import get_map
from classes.Object.Creature.NPC.NPC import NPC
import time


def create_new_board(game, board_index):
    map_file = f'games_config/Map_drawing/level{board_index}_map.txt'
    board_map = get_map(map_file)

    board_height = len(board_map)
    board_width = len(board_map[2])

    board = Board.board_switcher(
        board_index=board_index,
        game=game,
        board_map=board_map,
        width=board_width,
        height=board_height,
        hero=game.hero)

    return board
