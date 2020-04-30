from utils.data_manager import create_new_folder
from games_config.new_hero_creator import create_new_hero
from classes.Game.Game import Game
from games_config.board_factory import create_new_board


def create_new_game_mock():
    player_name = "PAWEL"
    game_name = "NEW_GAME"
    difficulty_level = 1

    create_new_folder(f'db/saves/{player_name}/{game_name}')
    create_new_folder(f'db/saves/{player_name}/{game_name}/BOARDS')
    create_new_folder(f'db/saves/{player_name}/{game_name}/BOARDS/BOARD0')

    hero = create_new_hero()
    game = Game(player_name=player_name,
                game_name=game_name,
                difficulty_level=difficulty_level,
                start_board_index=0,
                hero=hero)
    start_board = create_new_board(game, board_index=0)
    game.boards.append(start_board)
    return game
