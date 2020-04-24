from games_config.Monsters import *
from classes.Board.GameBoard import Board
from classes.Board.Fields import get_map


def create_new_board(game, board_index, loading=False):
    map_file = f'games_config/Map_drawing/level{board_index}_map.txt'

    board_map = get_map(map_file)

    board_height = len(board_map)
    board_width = len(board_map[2])
    # game.hero.position_x = 0
    # game.hero.position_y = 0

    board = Board(game, board_map=board_map,
                  width=board_width,
                  height=board_height,
                  hero=game.hero)
    if not loading:
        pass

    # # tu jakaś funkcja, która to poukłada,
    # board.monsters = [TROLL, TROLL, SNAKE, GIANT]
    # board.npc = []
    # board.items = []
    return board
