from macros import DIFFICULTY_LEVEL
from utils.validation import int_input
from games_config.new_hero_creator import create_new_hero
from games_config.board_factory import create_new_board
from classes.Game.Game import Game


def create_new_game(player_name):
    # GAME HISTORY?
    print('Welcome in our game!')
    # game_name = input('Please input folder name for saves: \n'
    #                   '> ')
    game_name = "PAWEL"  # MOCK
    create_new_folder(f'db/saves/{player_name}/{game_name}')
    create_new_folder(f'db/saves/{player_name}/{game_name}/BOARDS')
    create_new_folder(f'db/saves/{player_name}/{game_name}/BOARDS/BOARD0')
    print('Please choose difficulty level: ')
    choose_difficult = int_input('[1] EASY\n'
                                 '[2] NORMAL\n'
                                 '[3] HARD\n'
                                 '[4] IMPOSSIBLE\n'
                                 '> ', number_of_options=4)
    if choose_difficult == 1:
        difficulty_level = DIFFICULTY_LEVEL.EASY
    elif choose_difficult == 2:
        difficulty_level = DIFFICULTY_LEVEL.NORMAL
    elif choose_difficult == 3:
        difficulty_level = DIFFICULTY_LEVEL.HARD
    elif choose_difficult == 4:
        difficulty_level = DIFFICULTY_LEVEL.IMPOSSIBLE

    hero = create_new_hero()
    game = Game(player_name=player_name,
                game_name=game_name,
                difficulty_level=difficulty_level,
                start_board_index=0,
                hero=hero)
    start_board = create_new_board(game, board_index=0)
    game.boards.append(start_board)
    return game
