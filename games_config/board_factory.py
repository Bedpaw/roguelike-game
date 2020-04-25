from classes.Object.Creature.Monster.Monsters import Monster
from classes.Board.GameBoard import Board
from classes.Board.Fields import get_map
from classes.Object.Creature.NPC.NPC import NPC


def create_new_board(game, board_index, loading=False):
    map_file = f'games_config/Map_drawing/level{board_index}_map.txt'

    board_map = get_map(map_file)

    board_height = len(board_map)
    board_width = len(board_map[2])

    board = Board(game, board_map=board_map,
                  width=board_width,
                  height=board_height,
                  hero=game.hero)
    if not loading:
        board.monsters = [
            Monster.troll(7, 7, game.difficulty_level),
            Monster.rat(9, 7)
         ]
        board.npc = [NPC("Guard", "G", 1, 3)]
    return board
