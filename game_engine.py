from classes.Game.Game import Game
from classes.Object.Creature.Hero.Hero import Hero


def game_engine(user_choice):
    if user_choice == 1:    # new game
        game = Game()
        hero = game.create_hero()   # maybe this function shouldn't be in class Game?
    else:
        print("IN PROGRESS")    # load game data from files

    board = game.current_board()

    # MAIN GAME LOOP HERE
