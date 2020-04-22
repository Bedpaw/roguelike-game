from classes.Board import GameBoard
from classes.Object.Creature.Hero.Hero import Hero
from utils.utils import clear_screen

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 15
BOARD_HEIGHT = 8


def main():
    my_board = GameBoard.Board(BOARD_WIDTH, BOARD_HEIGHT, Hero('Pawel', '@', 0, 0))
    while True:
        my_board.update_board()
        my_board.print_board()
        my_board.get_user_choice()
        my_board.move_monsters()
        clear_screen()

        #   TEST
        hero = my_board.hero
        print(f'STR: {hero.strength},'
              f' LUCK: {hero.luck},'
              f' AGL: {hero.agility},'              
              f' HP: {hero.hp}/{hero.max_hp},'
              f' Lvl: {hero.level},'
              f' exp: {hero.exp}/{hero.exp_to_next_level}')
        print(f'X: {my_board.pos_x}')  # up down
        print(f'Y: {my_board.pos_y}')  # right left
        if my_board.monsters:
            print(f'M_X: {my_board.monsters[0].position_x}')
            print(f'M_Y: {my_board.monsters[0].position_y}')


if __name__ == '__main__':
    main()
