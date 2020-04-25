from classes.Object.Creature.Monster.Monsters import Monster
from classes.Board.GameBoard import Board
from classes.Board.Fields import *
from classes.Object.Creature.NPC.NPC import NPC


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

        board.monsters = [
            Monster.troll(7, 7, game.difficulty_level),
            Monster.troll(7, 6, game.difficulty_level),
            Monster.snake(7, 5, game.difficulty_level),
            Monster.giant(7, 4, game.difficulty_level),
            Monster.rat(9, 7)
        ]
        board.npc = [NPC("Guard", "G", 1, 3)]
        board.items = []
    return board
