from macros import DIFFICULTY_LEVEL
from utils.validation import int_input
from utils.data_manager import *
from games_config.new_hero_creator import create_new_hero
from games_config.board_factory import create_new_board
from classes.Game.Game import Game
from utils.hero_selection import get_user_hero_choice


def create_new_game(player_name):
    # GAME HISTORY?
    print('Welcome in our game!')
    create_new_folder(f'db/saves/{player_name}')

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
                game_name="RESUME_GAME",
                difficulty_level=difficulty_level,
                start_board_index=0,
                hero=hero)
    start_board = create_new_board(game, board_index=0)
    game.boards.append(start_board)
    return game
