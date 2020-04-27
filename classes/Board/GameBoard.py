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
        self.logo = 'Ziomeczki & ziomale'

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
                    battle(self.hero, caller, BATTLE_MODES.IMMEDIATE_FIGHT)
                    self.monsters.remove(caller)  # Not sure if this will work with many monsters
                    return True

            # monster vs npc validation
            # item in the feature(monster i hero)
            return True

    def get_user_choice(self):
        valid_key = False  # change to True if key is valid AND move is possible
        while not valid_key:
            key_pressed = key_service.key_pressed()

            if key_pressed in ['w', 's', 'a', 'd', 'p', 'm', 'o']:

                if key_pressed == 'p':
                    exit()
                if key_pressed == 'o':
                    cprint("Game saved...", wait_after=1)
                    self.game.save_game()
                elif key_pressed == 'm':
                    self.hero.show_stats_breed()
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
        border_field = f"{BG_COLOR.BLUE}  {STYLES.RESET}"

        # MIDDLE LOGIC
        middle_border = []
        max_row_length = 0

        for i, list_of_fields in enumerate(self.game_board_in_class):

            if i == 0:
                middle_fileds = f"{border_field}{' ' * 5}"
            elif i == 1 or i == self.height + 1:
                middle_fileds += ''
            else:
                middle_fileds = f"\n{border_field}{' ' * 6}"

            for j, field in enumerate(list_of_fields):
                if field.symbol_on_map not in symbols_to_txt_draw.keys():
                    middle_fileds += self.board_map[i-1][j].field_color + field.color_on_board + field.symbol_on_map + STYLES.RESET
                else:
                    middle_fileds += field.field_color + field.symbol_on_map + STYLES.RESET

            additonal_info = ''

            if i == 1:
                additonal_info = f"{' '*2}Nickname: {self.hero.name}  "
            if i == 3:
                additonal_info = f"{' '*2}Class: {self.hero.breed}  "
            if i == 4:
                additonal_info = f"{' '*2}HP: {self.hero.hp}/{self.hero.max_hp}  "
            if i == 5:
                additonal_info = f"{' '*2}MANA: {self.hero.hp}/{self.hero.max_hp}  "
            if i == 6:
                additonal_info = f"{' '* 2}EXP: {self.hero.exp}/{self.hero.exp_to_next_level}  "
            if i == 7:
                additonal_info = f"{' ' * 2}CORDS: x:{self.hero.position_x} | y:{self.hero.position_y}"
                additonal_info += f"{' ' *(6 - len(str(self.hero.position_x)) - len(str(self.hero.position_y)))}"

            middle_fileds += additonal_info

            if i is len(self.game_board_in_class) - 1:
                row_length = self.width + 11 + len(additonal_info)
            else:
                row_length = self.width + 10 + len(additonal_info)
            if i not in [0, len(self.game_board_in_class) - 2]:
                middle_border.append([row_length, middle_fileds])

            if row_length > max_row_length:
                max_row_length = row_length

        if len(self.name) + 2 > max_row_length:
            max_row_length = len(self.name) + 2


        # GENERAL
        new_empty_line = f"\n{border_field}{' ' * (max_row_length -4)}{border_field}"
        # TOP PRINT AND LOGIC
        map_name = f"{border_field}{' ' * 2}Mapa: {self.name}{' ' * (max_row_length - len(self.name) - 12)}{border_field}"
        top = f"{BG_COLOR.BLUE}{' ' * max_row_length}{STYLES.RESET}\n"
        logo = f"{border_field}{' ' * 2}{self.logo}{STYLES.RESET}{' ' * (max_row_length - len(self.logo)-6)}{border_field}\n"
        top += logo + map_name + new_empty_line
        print(top)

        # MIDDLE
        mid = []
        for i, item in enumerate(middle_border):
            mid.append(f"{item[1]}{' ' * (max_row_length - item[0])}{border_field}")
        print(''.join(mid), new_empty_line)


        # LAST MESSAGE FROM HERO
        # TODO

        # BOTTOM PRINT AND LOGIC
        # print(f"{border_field}{' ' * (max_row_length -4)}{border_field}")
        print(f"{new_empty_line[1:]}\n{BG_COLOR.BLUE}{' ' * max_row_length}{STYLES.RESET}")


