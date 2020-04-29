from classes.Board.Fields import *
from random import randint
import copy
from macros import OBJECT_TYPES, BATTLE_MODES, MOVES_TYPES
from utils import key_service
from utils.decorations import cprint
from macros.COLORS import *
from events.Battle import battle
from classes.Board.Fields import Field
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.NPC.NPC import NPC
from classes.Object.Creature.Monster.Monster import Monster
from utils.sounds import play_music, pause_music, unpause_music

import time


class Board:
    def __init__(self, game, board_map, width, height, hero):
        self.game = game
        self.width = width
        self.height = height
        self.board_map = board_map
        # hero
        self.hero = hero
        self.player_sign = hero.symbol_on_map
        self.pos_x = hero.position_x
        self.pos_y = hero.position_y
        # --------------------------------
        self.game_board_in_class = [[Field()]] + copy.deepcopy(self.board_map) + [[Field()]]
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero
        self.name = "Mongolscy przemytnicy rzeżuchy"
        self.monsters = []
        self.npc = []
        self.treasures = []

    def special_ground_effect(self):
        pass

    def update_board(self):
        self.make_empty_list()
        self.add_object_to_board(self.monsters)
        self.add_object_to_board(self.npc)
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero
        self.hero.position_x = self.pos_x
        self.hero.position_y = self.pos_y

    def move_monsters(self):
        for monster in self.monsters:
            valid = False
            moves_counter = 0
            while not valid:
                x, y = monster.move(params=monster.move_param)
                # Skip move if no valid option in 10 trys
                moves_counter += 1
                if moves_counter == 10:
                    valid = True
                if self.check_move_possibility(monster, x, y):
                    monster.position_x = x
                    monster.position_y = y
                    valid = True

    def make_empty_list(self):
        clear_list = copy.deepcopy(self.board_map)
        self.game_board_in_class = [[Field()]] + clear_list + [[Field()]]

    def add_object_to_board(self, object_items):
        for object_item in object_items:
            self.game_board_in_class[object_item.position_x][object_item.position_y] = object_item

    def check_move_possibility(self, caller, positionX, positionY):
        """
        :param caller:Hero or Monster
        :param positionX:VERTICAL ^
        :param positionY:HORIZONTAL <->
        :return: True if move is possible, False if it isn't
        """

        # Idea for making one for for checking everything instead for loops do it by checking proper value in given caller
        if positionX < 1 or positionY < 0 or positionY > self.width - 1 or positionX > self.height:
            return False

        check_position = self.game_board_in_class[positionX][positionY]  # after 1 if, because index out of range

        if not check_position.field_move_possible:
            return False

        else:
            if isinstance(caller, Hero):

                for i, monster in enumerate(self.monsters):
                    if monster.position_x == positionX and monster.position_y == positionY:
                        cprint(f"You attacked {monster.name}!", ERROR, start_enter=1, wait_after=1)
                        battle(caller, monster, BATTLE_MODES.IMMEDIATE_FIGHT)
                        if not monster.is_on_board:
                            del self.monsters[i]
                        return True
                for i, one_npc in enumerate(self.npc):
                    if one_npc.position_x == positionX and one_npc.position_y == positionY:
                        if one_npc.on_meet(self.hero):  # return True if hero start fight with NPC else False
                            if not one_npc.is_on_board:
                                del self.npc[i]
                                return True
                        return False

            elif isinstance(caller, Monster):
                if isinstance(check_position, NPC) or isinstance(check_position, Monster):
                    return False
                if self.pos_x == positionX and self.pos_y == positionY:
                    cprint(f'{self.hero.name} has been attacked by {caller.name}!', ERROR, start_enter=1, wait_after=1)
                    # pause_music()
                    battle(self.hero, caller, BATTLE_MODES.IMMEDIATE_FIGHT)
                    # unpause_music()
                    self.monsters.remove(caller)  # Not sure if this will work with many monsters
                    return True

            # monster vs npc validation
            # item in the feature(monster i hero)
            return True

    def get_user_choice(self):
        valid_key = False  # change to True if key is valid AND move is possible
        while not valid_key:
            key_pressed = key_service.key_pressed()

            if key_pressed in ['w', 's', 'a', 'd', 'p', 'o']:
                if key_pressed == 'p':
                    exit()
                if key_pressed == 'o':
                    cprint("Game saved...", wait_after=1)
                    self.game.save_game()

                # Move from first gate
                elif key_pressed == 'd' and self.pos_x == 0 and self.pos_y == 0:
                    self.pos_x += 1
                    valid_key = True
                # Move to previous board
                elif self.pos_x == 1 and self.pos_y == 0 and key_pressed == 'a':
                    if self.game.current_board_index != 0:
                        self.game.previous_board()
                        valid_key = True
                # Move to next board
                elif self.pos_x == self.height and self.pos_y == self.width - 1 and key_pressed == 'd':
                    self.game.next_board()
                    valid_key = True
                # Normal move
                else:
                    new_x_pos, new_y_pos = self.hero.move(key_pressed)
                    if self.check_move_possibility(self.hero, new_x_pos, new_y_pos):
                        self.pos_x = new_x_pos
                        self.pos_y = new_y_pos
                        valid_key = True

    def print_board(self):
        # overscore = "\u203e"

        # MIDDLE
        for i, list_of_fields in enumerate(self.game_board_in_class):
            if i == 0:
                middle_fileds = f"{' ' * 5}"
            elif i == 1 or i == self.height + 1:
                middle_fileds += ''
            else:

                middle_fileds += f"\n{' ' * 6}"

            for field in list_of_fields:
                # print(field)
                # if field.symbol_on_map == '0':
                #     middle_fileds += BG_COLOR.GREEN + ' ' + STYLES.RESET
                # else:
                middle_fileds += field.field_color + field.symbol_on_map + STYLES.RESET

            # elif i == len(self.game_board_in_class)-3:
            #     middle_fileds += '|_\n'
            # elif i == len(self.game_board_in_class)-2:
            #     middle_fileds += ''
            # elif i == len(self.game_board_in_class)-1:
            #     middle_fileds += ''

            # else:
            #     middle_fileds += '|\n'

        print(middle_fileds, sep='')

        # BOTTOM
        # print(f"{' '*13}{overscore*(self.width+3)}\n")

    def random_free_position(self):
        free_position = False
        while not free_position:
            y = randint(0, self.width - 1)
            x = randint(1, self.height)
            if isinstance(self.game_board_in_class[x][y], Field):
                return x, y

    def add_object_in_random_pos(self, init_func, count=1):
        for i in range(count):
            self.update_board()
            x, y = self.random_free_position()
            obj = init_func(x, y, self.game.difficulty_level)
            if isinstance(obj, Monster):
                self.monsters.append(obj)

    @classmethod
    def board_switcher(cls, board_id, game, board_map, width, height, hero):
        board = cls(game, board_map, width, height, hero)

        def switcher(board_id):
            boards = {
                "0": labirynth,
                "1": plain,
                "2": troll_cave_entry,
                "3": troll_cave,
                "4": the_great_bridge,
                "5": city
            }
            return boards[str(board_id)]()

        def labirynth():
            board.name = "Labyrynth"
            board.monsters = [
                Monster.troll(7, 7, game.difficulty_level),
                Monster.rat(9, 7)
            ]
            return board

        def plain():
            board.name = "Plain"
            board.npc = [NPC("Guard", "G", 4, 8), NPC('Guard', 'G', 4, 10)]
            board.add_object_in_random_pos(Monster.rat, count=4)
            board.add_object_in_random_pos(Monster.snake, count=4)
            return board

        def troll_cave_entry():
            board.name = "Troll cave entry"
            board.monsters = [
                Monster.troll(2, 5, game.difficulty_level),
                Monster.troll(5, 12, game.difficulty_level),
                Monster.troll(9, 8, game.difficulty_level),
            ]
            board.monsters[0].move_type = MOVES_TYPES.STAY
            board.monsters[1].move_type = MOVES_TYPES.STAY
            board.monsters[2].move_type = MOVES_TYPES.STAY
            board.add_object_in_random_pos(Monster.rat)
            board.add_object_in_random_pos(Monster.rat)
            return board

        def troll_cave():
            board.name = "Troll cave"
            board.monsters = [Monster.troll_warrior(1, 2, game.difficulty_level),
                              Monster.troll(4, 5, game.difficulty_level),
                              Monster.troll(6, 5, game.difficulty_level),
                              Monster.troll(5, 6, game.difficulty_level),
                              Monster.troll(5, 4, game.difficulty_level)
                              ]
            board.monsters[0].move_type = MOVES_TYPES.STAY
            board.npc = [
                NPC.troll_king(5, 5, game.difficulty_level)
            ]
            return board

        def the_great_bridge():
            board.name = "The great bridge"
            board.add_object_in_random_pos(Monster.rat, count=6)

            return board

        def city():
            board.name = "City"

            return board

        return switcher(board_id)
