from classes.Board.Fields import *
from random import randint, choice
import copy
import math
from macros import OBJECT_TYPES, BATTLE_MODES, MOVES_TYPES
from utils import key_service
from macros.COLORS import *
from events.Battle import battle
from classes.Board.Fields import Field
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.NPC.NPC import NPC
from classes.Object.Creature.NPC.NPCS import NPCS
from classes.Object.Creature.Monster.Monster import Monster
from classes.Object.Item.Item import Treasure
from utils.sounds import play_music, pause_music, unpause_music
import time
from utils.utils import clear_screen
from menu.pause_menu import pause_game_menu


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
        self.name = "Set_me_name"
        self.last_move_message = []
        self.monsters = []
        self.npc = []
        self.treasures = []
        self.logo = "ANGRY TROLLS!"         # :TODO W -> delete?
        self.is_boss_on_map = False

    def special_ground_effect(self):
        pass

    def update_board(self):
        self.make_empty_list()
        self.add_object_to_board(self.monsters)
        self.add_object_to_board(self.npc)
        self.add_object_to_board(self.treasures)
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero
        self.hero.position_x = self.pos_x
        self.hero.position_y = self.pos_y

    def move_monsters(self):
        for monster in self.monsters:
            if not self.hero.is_alive():
                break
            valid = False
            moves_counter = 0
            while not valid:
                x, y = monster.move(params=monster.move_param)
                # Skip move if no valid option in 10 trys
                moves_counter += 1
                if moves_counter == 50:
                    valid = True
                if self.check_move_possibility(monster, x, y):

                    monster.position_x = x
                    monster.position_y = y
                    self.update_board()
                    valid = True

    def make_empty_list(self):
        clear_list = copy.deepcopy(self.board_map)
        self.game_board_in_class = [[Field()]] + clear_list + [[Field()]]

    def add_object_to_board(self, object_items):
        for object_item in object_items:
            self.game_board_in_class[object_item.position_x][object_item.position_y] = object_item

    def lava_detector(self):
        self.hero.hp -= 20
        if not self.hero.is_alive():
            self.game.endgame = True
        self.last_move_message.append(Fire.on_move_message)
        pass

    def check_move_possibility(self, caller, positionX, positionY):
        """
        :param caller:Hero or Monster
        :param positionX:VERTICAL ^
        :param positionY:HORIZONTAL <->
        :return: True if move is possible, False if it isn't
        """
        # BOARD BORDERS
        if positionX < 1 or positionY < 0 or positionY > self.width - 1 or positionX > self.height:
            if isinstance(caller, Hero):
                self.last_move_message.append(f" You hit a wall! {self.hero.name}: AUU!")
                self.print_board()
            return False
        obj_in_pos = self.game_board_in_class[positionX][positionY]
        if not obj_in_pos.field_move_possible:
            self.last_move_message.append(obj_in_pos.on_move_message)
            self.print_board()
            return False

        elif isinstance(caller, Hero):
            if isinstance(obj_in_pos, Fire):
                self.lava_detector()
                return True
            if isinstance(obj_in_pos, NPC):
                if obj_in_pos.on_meet(self.hero):  # return True if hero start fight with NPC else False
                    self.npc.remove(obj_in_pos)
                    return True
                self.print_board()
                return False
            elif isinstance(obj_in_pos, Treasure):
                if obj_in_pos.open_treasure(self.hero):  # return True if hero took treasure
                    self.treasures.remove(obj_in_pos)
                    return True
                # self.print_board()
                return False
            elif isinstance(obj_in_pos, Monster):
                battle(caller, obj_in_pos, self.game.battle_mode)
                self.monsters.remove(obj_in_pos)
                return True

        elif isinstance(caller, Monster):
            if isinstance(obj_in_pos, Fire):
                return False
            if isinstance(obj_in_pos, NPC) or isinstance(obj_in_pos, Monster) or isinstance(obj_in_pos, Treasure):
                return False
            elif isinstance(obj_in_pos, Hero):
                battle(obj_in_pos, caller, self.game.battle_mode, hero_start=False)
                self.monsters.remove(caller)
                return True
        return True

    def get_user_choice(self):
        valid_key = False  # change to True if key is valid AND move is possible
        while not valid_key:
            # self.print_last_message()
            key_pressed = key_service.key_pressed()

            if key_pressed in ['w', 's', 'a', 'd', 'p', 'm', 'o', 'x', 'z', 'j', 'h', 'i']:
                # Z and X are cheats for testing
                if key_pressed == 'z':
                    self.pos_x = 1
                    self.pos_y = 0
                elif key_pressed == 'x':
                    self.pos_x = self.height
                    self.pos_y = self.width - 1
                elif key_pressed == 'p':
                    pause_game_menu(self.game)
                elif key_pressed == 'o':
                    self.game.save_game()
                elif key_pressed == 'j':
                    if self.hero.points_for_level == 0:
                        self.hero.show_stats_breed()
                    elif self.hero.points_for_level > 0:
                        self.hero.show_stats_with_add_points()
                        self.print_board()
                elif key_pressed == "h":
                    self.hero.use_hpotion("healing_potion")
                    self.print_board()
                elif key_pressed == "m":
                    self.hero.use_mana("mana")
                    self.print_board()
                elif key_pressed == "i":
                    self.hero.print_inventory()

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
                        self.update_board()
                        valid_key = True

    def print_board(self):
        self.update_board()
        clear_screen()
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
                    middle_fileds += self.board_map[i - 1][
                                         j].field_color + field.color_on_board + field.symbol_on_map + STYLES.RESET
                else:
                    middle_fileds += field.field_color + field.color_on_board + field.symbol_on_map + STYLES.RESET

            additonal_info = ''

            if i == 1:
                additonal_info = f"{' ' * 2}Nickname: {self.hero.name}  "
            if i == 2:
                additonal_info = f"{' ' * 2}Level: {self.hero.level}  "
            if i == 3:
                additonal_info = f"{' ' * 2}Class: {self.hero.breed}  "
            if i == 4:
                additonal_info = f"{' ' * 2}HP: {int(self.hero.hp)}/{int(self.hero.max_hp)}  "
            if i == 5:
                additonal_info = f"{' ' * 2}MANA: {int(self.hero.mana)}/{int(self.hero.max_mana)}  "
            if i == 6:
                additonal_info = f"{' ' * 2}EXP: {self.hero.exp}/{self.hero.exp_to_next_level}  "
            if i == 7:
                additonal_info = f"{' ' * 2}CORDS: x:{self.hero.position_x} | y:{self.hero.position_y}"
                additonal_info += f"{' ' * (6 - len(str(self.hero.position_x)) - len(str(self.hero.position_y)))}"
            if i == 8:
                if self.hero.points_for_level > 0:
                    additonal_info = f"{' ' * 2}Press [j] to add points  "
            if i == 9:
                additonal_info = f"{' ' * 2}|H|:HP |M|:MANA |I|:Inventory"

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
        new_empty_line = f"\n{border_field}{' ' * (max_row_length - 4)}{border_field}"
        # TOP PRINT AND LOGIC
        map_name = f"{border_field}{' ' * 2}Mapa: {self.name}{' ' * (max_row_length - len(self.name) - 12)}{border_field}"
        top = f"{BG_COLOR.BLUE}{' ' * max_row_length}{STYLES.RESET}\n"
        logo = f"{border_field}{' ' * 2}{self.logo}{STYLES.RESET}{' ' * (max_row_length - len(self.logo) - 6)}{border_field}\n"
        top += logo + map_name + new_empty_line
        print(top)

        # MIDDLE
        mid = []
        for i, item in enumerate(middle_border):
            mid.append(f"{item[1]}{' ' * (max_row_length - item[0])}{border_field}")
        print(''.join(mid), new_empty_line)

        # LAST MESSAGE FROM HERO
        if not self.is_boss_on_map:
            nothing_happened_messages = ["Nothing happened... this time around",
                                         f"{self.hero.name}: Did I hear something?",
                                         "Angry trolls are watching you...",
                                         "Such a strange place...",
                                         f"{self.hero.name}: I hear hudge creatures near here",
                                         f"{self.hero.name}: What was that?!",
                                         "Keep rolin' rolin'",
                                         f"{self.hero.name}: Toss a coin to your {self.hero.name}... nanana"
                                         ]
        else:
             nothing_happened_messages = ["Belzedup: Hahahaa, I will eat your brain",
                                          "Belzdup: XXXDDD",
                                          "Belzedup: 666! 666!",
                                          "Belzedup: Come here, I'm waiting for you!"

                                     ]
        if not self.last_move_message:
            self.last_move_message.append(choice(nothing_happened_messages))
        for last_message in self.last_move_message:
            number_of_lines = math.ceil(len(last_message)/(max_row_length-6))
            one_line_len = int(len(last_message)/number_of_lines)

            last_message_chunks = [last_message[i: i + one_line_len]
                                   for i in range(0, len(last_message), one_line_len)]

            last_message_chunks = [f"{border_field}{' '* int((max_row_length - 4 - math.ceil(len(item)))/2)}{item}" \
                                   f"{' '* int((max_row_length - 3 - math.floor(len(item)))/2)}{border_field}"
                                   for item in last_message_chunks]
        last_message_chunks = [f"{BG_COLOR.BLUE}{' ' * max_row_length}{STYLES.RESET}"] + last_message_chunks
        print('\n'.join(last_message_chunks))
        self.last_move_message = []

        print(f"{new_empty_line[1:]}\n{BG_COLOR.BLUE}{' ' * max_row_length}{STYLES.RESET}")


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
    def board_switcher(cls, board_id, game, board_map, width, height, hero, loading):
        board = cls(game, board_map, width, height, hero)

        def switcher(board_id):
            boards = {
                "0": labyrinth,
                "1": plain,
                "2": troll_cave_entry,
                "3": troll_cave,
                "4": the_great_bridge,
                "5": city,
                "6": highway_to_hell,
                "7": demonic_maze
            }
            if loading:
                board.name = boards[str(board_id)].__name__ # :TODO useless probably
                return board
            else:
                return boards[str(board_id)]()

        def labyrinth():
            board.name = "Labyrinth"
            board.last_move_message.append(f"Hm... very nice place")

            board.monsters = [
                Monster.troll(1, 3, game.difficulty_level),
                Monster.rat(9, 7),
                Monster.troll(7, 7, game.difficulty_level),
            ]
            board.treasures = [
                Treasure(position_x=10, position_y=0)
            ]
            return board

        def plain():
            board.name = "Plain"
            board.last_move_message.append(f"I see guards here, let's talk with them!")
            board.npc = [
                NPC("Guard", "G", 4, 8),
                NPC('Guard', 'G', 4, 10)
            ]
            board.treasures = [
                Treasure(position_x=5, position_y=8, is_locked=True),
                Treasure(position_x=5, position_y=10)
            ]
            board.add_object_in_random_pos(Monster.rat, count=1)
            board.add_object_in_random_pos(Monster.snake, count=1)

            return board

        def troll_cave_entry():
            board.name = "Troll cave entry"
            board.last_move_message.append(f"Such a stinky place...")
            board.monsters = [
                Monster.troll(2, 5, game.difficulty_level),
                Monster.troll(5, 12, game.difficulty_level),
                Monster.troll(9, 8, game.difficulty_level),
            ]
            board.treasures = [
                Treasure(position_x=4, position_y=15),
                Treasure(position_x=7, position_y=15, is_locked=True)
            ]
            board.monsters[0].move_type = MOVES_TYPES.STAY
            board.monsters[1].move_type = MOVES_TYPES.STAY
            board.monsters[2].move_type = MOVES_TYPES.STAY
            board.add_object_in_random_pos(Monster.rat, count=2)

            return board

        def troll_cave():
            board.name = "Troll cave"
            board.last_move_message.append(f"Yay, Trolls everywhere!")
            board.monsters = [
                Monster.troll_warrior(1, 2, game.difficulty_level),
                Monster.troll(4, 5, game.difficulty_level),
                Monster.troll(6, 5, game.difficulty_level),
                Monster.troll(5, 6, game.difficulty_level),
                Monster.troll(5, 4, game.difficulty_level)
            ]
            board.npc = [
                NPCS.troll_king(5, 5, game.difficulty_level),
                NPCS.fake_wall(6, 11, name="Hole in the wall"),
            ]
            board.monsters[0].move_type = MOVES_TYPES.STAY

            return board

        def the_great_bridge():
            board.name = "The great bridge"
            board.last_move_message.append(f"I like to swim, but not today")
            board.add_object_in_random_pos(Monster.snake, count=2)
            return board

        def city():
            board.name = "City"
            board.last_move_message.append(f"Thanks God! Normal people around!")
            board.npc = [
                NPCS.king(1, 10),
                NPC("Guard", "G", 2, 6),
                NPC('Guard', 'G', 2, 14)
                #  NPC.eastern_guard(11, 20)
            ]
            board.treasures = [
                Treasure(position_x=1, position_y=4),
                Treasure(position_x=1, position_y=5),
                Treasure(position_x=1, position_y=15),
                Treasure(position_x=1, position_y=16),
            ]
            board.add_object_in_random_pos(Monster.rat, count=3)
            return board

        def highway_to_hell():
            board.name = "highway_to_hell"
            board.last_move_message.append(f"This place was made for such a creatures")
            board.monsters = [Monster.troll_warrior(1, 2, game.difficulty_level),
                              Monster.rat(4, 5, game.difficulty_level),
                              Monster.troll_warrior(7, 15, game.difficulty_level),
                              Monster.rat(11, 8, game.difficulty_level)
                              ]
            board.treasures = [Treasure(position_x=7, position_y=4, is_locked=True),
                               Treasure(position_x=5, position_y=11)]
            return board

        def demonic_maze():
            board.name = "Demonic maze"
            board.last_move_message.append(f"I feel odour of sulfur and death")
            board.is_boss_on_map = True
            board.monsters = [Monster.troll_warrior(1, 18, game.difficulty_level),
                              Monster.rat(3, 10, game.difficulty_level),
                              Monster.troll_warrior(7, 15, game.difficulty_level),
                              Monster.troll_warrior(2, 2, game.difficulty_level)
                              ]
            board.treasures = [Treasure(position_x=2, position_y=18, is_locked=True),
                               Treasure(position_x=8, position_y=20),
                               Treasure(position_x=2, position_y=10, is_locked=True)
                               ]
            return board

        return switcher(board_id)

