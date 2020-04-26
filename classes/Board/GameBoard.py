from classes.Board.Fields import *
import copy
from macros import OBJECT_TYPES, BATTLE_MODES
from utils import key_service
from utils.decorations import cprint
from macros.COLORS import *
from events.Battle import battle
from classes.Board.Fields import Field
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.NPC.NPC import NPC
from classes.Object.Creature.Monster.Monster import Monster


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
            while not valid:
                x, y = monster.move()
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
        elif self.game_board_in_class[positionX][positionY].field_move_possible == False:
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
                                # return True
                            return True

            elif isinstance(caller, Monster):
                if isinstance(self.game_board_in_class[positionX][positionY], NPC):
                    return False

                elif self.pos_x == positionX and self.pos_y == positionY:
                    cprint(f'{self.hero.name} has been attacked by {caller.name}!', ERROR, start_enter=1, wait_after=1)
                    battle(self.hero, caller, BATTLE_MODES.IMMEDIATE_FIGHT)
                    self.monsters.remove(caller)    # Not sure if this will work with many monsters
                    return True

            # monster vs npc validation
            # item in the feature(monster i hero)
            return True

    def get_user_choice(self):
        valid_key = False  # change to True if key is valid AND move is possible
        while not valid_key:
            key_pressed = key_service.key_pressed()

            if key_pressed in ['w', 's', 'a', 'd', 'p']:
                if key_pressed == 'p':
                    exit(0)

                # Move from first gate
                elif key_pressed == 'd' and self.pos_x == 0 and self.pos_y == 0:
                    self.pos_x += 1
                    valid_key = True
                elif self.pos_x == 1 and self.pos_y == 0 and key_pressed == 'a':
                    if self.game.current_board_index != 0:
                        self.game.previous_board()
                        valid_key = True

                elif self.pos_x == self.height and self.pos_y == self.width-1 and key_pressed == 'd':
                    self.game.next_board()
                    valid_key = True


                else:
                    new_x_pos, new_y_pos = self.hero.move(key_pressed)  # hero.move trick to work with Y, X cords
                    if self.check_move_possibility(self.hero, new_x_pos, new_y_pos):
                        self.pos_x = new_x_pos
                        self.pos_y = new_y_pos
                        valid_key = True

    def print_board(self):
        for i, list_of_fields in enumerate(self.game_board_in_class):
            if i == 0:
                middle_fileds = f"{' ' * 5}"
            elif i == 1 or i == self.height + 1:
                middle_fileds += ''
            else:

                middle_fileds += f"\n{' ' * 6}"

            for j, field in enumerate(list_of_fields):
                if field.symbol_on_map not in symbols_to_txt_draw.keys():
                    middle_fileds += self.board_map[i-1][j].field_color + field.color_on_board + field.symbol_on_map + STYLES.RESET
                else:
                    middle_fileds += field.field_color + field.symbol_on_map + STYLES.RESET


        print(middle_fileds, sep='')

        # BOTTOM
        # print(f"{' '*13}{overscore*(self.width+3)}\n")