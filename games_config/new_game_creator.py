from classes.Game.Game import Game
from games_config.new_hero_creator import create_new_hero
from games_config.board_factory import create_new_board

from utils.utils import clear_screen
from utils.validation import int_input
from utils.data_manager import create_new_folder
from macros import DIFFICULTY_LEVEL


def create_new_game(player_name):
    clear_screen()
    create_new_folder(f'db/saves/{player_name}')

    choose_difficult = int_input('Please choose difficulty level:\n'
                                 '[1] EASY\n'
                                 '[2] NORMAL\n'
                                 '[3] HARD\n'
                                 '[4] IMPOSSIBLE\n\n'
                                 'Your choice: ', number_of_options=4)
    if choose_difficult == 1:
        difficulty_level = DIFFICULTY_LEVEL.EASY
    elif choose_difficult == 2:
        difficulty_level = DIFFICULTY_LEVEL.NORMAL
    elif choose_difficult == 3:
        difficulty_level = DIFFICULTY_LEVEL.HARD
    elif choose_difficult == 4:
        difficulty_level = DIFFICULTY_LEVEL.IMPOSSIBLE

    hero = create_new_hero(player_name)
    game = Game(player_name=player_name,
                game_name="RESUME_GAME",
                difficulty_level=difficulty_level,
                start_board_index=0,
                hero=hero)
    hero.game = game
    start_board = create_new_board(game, board_index=0)
    game.boards.append(start_board)
    return game
