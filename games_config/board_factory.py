from classes.Object.Creature.Monster.Monsters import Monster
from classes.Board.GameBoard import Board
from classes.Board.Fields import get_map
from classes.Object.Creature.NPC.NPC import NPC
import time


def create_new_board(game, board_index, loading=False, current_board=False):
    map_file = f'games_config/Map_drawing/level{board_index}_map.txt'
    board_map = get_map(map_file)

    board_height = len(board_map)
    board_width = len(board_map[2])

    if not game.true_player_position and loading:
        game.true_player_position = [game.hero.position_x, game.hero.position_y]

    if game.true_player_position and loading:
        game.hero.position_x = 0
        game.hero.position_y = 0

    if current_board:
        if game.true_player_position:
            game.hero.position_x = game.true_player_position[0]
            game.hero.position_y = game.true_player_position[1]

    board = Board.board_switcher(
        board_id=board_index,
        game=game,
        board_map=board_map,
        width=board_width,
        height=board_height,
        hero=game.hero)

    if not loading:
        pass
    return board
