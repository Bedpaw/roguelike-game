from classes.Game.Game import Game
from utils.utils import clear_screen
from utils.data_manager import *
from games_config.new_game_creator import create_new_game
from classes.Object.Creature.Hero.Hero import Hero      # eval use it!!!


def load_game(player_name):
    game_name = get_game_name(player_name)
    game_difficulty_level, board_index, hero_class = read_game_config(player_name)
    path_with_hero_data = f'db/saves/{player_name}/{game_name}/hero.txt'
    print('board index in load game', board_index)
    hero = load_object_from_file(path_with_hero_data, eval(hero_class))
    game = Game(player_name=player_name,
                game_name=game_name,
                difficulty_level=game_difficulty_level,
                start_board_index=board_index,
                hero=hero)
    load_boards_to_game(game)
    return game


def game_engine(user_choice, player_name):
    if user_choice == 1:
        game = create_new_game(player_name)
    elif user_choice == 2:
        game = load_game(player_name)

    while not game.endgame:
        game.board_changed = False
        my_board = game.current_board()

        while not game.board_changed and not game.endgame:

            my_board.update_board()
            print(8 * " " + my_board.name)  # to change
            my_board.print_board()
            my_board.get_user_choice()
            my_board.move_monsters()
            clear_screen()  # should be right before print boards
            game.turn_counter += 1

            #   TEST
            #save_objects_from_board(f'{path_to_save_boards}{game.current_board_index}/', my_board)
            hero = my_board.hero  # for test shortcut

            print(f'TURN: {game.turn_counter}')
            print(f'STR: {hero.strength},'
                  f' LUCK: {hero.luck},'
                  f' AGL: {hero.agility},'
                  f' HP: {hero.hp}/{hero.max_hp},'
                  f' Lvl: {hero.level},'
                  f' exp: {hero.exp}/{hero.exp_to_next_level}')
            print(f'X: {my_board.pos_x} Y: {my_board.pos_y}')  # up down / right left
            if my_board.monsters:
                print(f'M_X: {my_board.monsters[0].position_x} M_Y: {my_board.monsters[0].position_y}')

    # game loop broken
    # hero is dead or game won2
    # final screen? # add to highscores


game_engine(1, "PAWEL")
