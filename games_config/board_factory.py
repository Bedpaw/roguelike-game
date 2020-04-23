from games_config.Monsters import *
from classes.Board.GameBoard import Board
from classes.Board.Fields import *


def create_new_board(game, board_index, loading=False):
    map_file = f'games_config/Map_drawing/level{board_index}_map.txt'

    def get_map(map_file_name=map_file):
        with open(map_file_name, 'r') as f:
            full_map = f.readlines()
            full_map_list = [list(item.strip()) for item in full_map]
            # print(full_map_list)
            list_of_all_fields = []
            for row in full_map_list:
                row_of_fields = []
                for i, elem in enumerate(row):
                    if elem == '0':
                        row_of_fields.append(Field())
                    elif elem == '-':
                        row_of_fields.append(Wall())
                    elif elem == '~':
                        row_of_fields.append(River())
                list_of_all_fields.append(row_of_fields)
            # print(full_map_list)
        return list_of_all_fields

    board_map = get_map()
    board_height = len(board_map)
    board_width = len(board_map[2])

    board = Board(board_map=board_map,
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
