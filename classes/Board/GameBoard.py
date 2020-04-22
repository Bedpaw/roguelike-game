from macros import OBJECT_TYPES, BATTLE_MODES
from classes.Object.Creature.Monster.Monsters import *
from classes.Object.Creature.Hero.Hero import Hero
from utils import key_service, data_manager
import time
from utils.decorations import cprint
from macros.COLORS import *
from events.Battle import battle
from classes.Board.Fields import Field
from classes.Object.Creature.NPC.NPC import NPC


class Board:
    def __init__(self, width, height, hero):
        self.width = width
        self.height = height
        self.name = "LAS TROLLI"
        # hero
        self.hero = hero
        self.player_sign = hero.symbol_on_map
        self.pos_x = hero.position_x
        self.pos_y = hero.position_y
        # --------------------------------
        self.game_board_in_class = [[self.player_sign]] + [[Field()] * self.width for i in range(self.height)] + [
            [Field()]]
        self.game_board_in_class[self.pos_x][self.pos_y] = self.player_sign
        self.load_objects_from_db()

    monsters = []
    npc = []
    # Troll('Wojtek', 'W', 2, 2), Troll('Wojtek', 'W', 8, 7),
    # NPC('Guard', 'S', 4, 0), NPC('Strażnik Sandomierza', 'S', 8, 14)
    def load_objects_from_db(self):
        data_manager.load_objects_to_board('db/saves/PAWEL/RESUME_GAME/BOARDS/BOARD0', self)


    def update_board(self):
        self.make_empty_list()
        self.add_object_to_board(self.monsters)
        self.add_object_to_board(self.npc)
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero
        self.hero.position_x = self.pos_x  # DONT TOUCH IT
        self.hero.position_y = self.pos_y  # DONT TOUCH IT

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
        self.game_board_in_class = [[Field()]] + [[Field()] * self.width for i in range(self.height)] + [[Field()]]

    def add_object_to_board(self, object_items):
        for item in object_items:
            self.game_board_in_class[item.position_x][item.position_y] = item

    def check_move_possibility(self, caller, positionX, positionY):
        """
        :param caller:Hero or Monster
        :param positionX:VERTICAL ^
        :param positionY:HORIZONTAL <->
        :return: True if move is possible, False if it isn't
        """
        # Idea for making one for for checking everything instead for loops do it by checking proper value in given caller

        # hero/monster -> wall
        if positionX < 1 or positionY < 0 or positionY > self.width - 1 or positionX > self.height:
            return False
        else:
            if isinstance(caller, Hero):  # TODO: Change to issubclass when Dwarf, Elf etc ready
                # hero -> monster
                for i, monster in enumerate(self.monsters):
                    if monster.position_y == positionY and monster.position_x == positionX:
                        cprint(f"You attacked {monster.name}!", ERROR, start_enter=1, wait_after=1)
                        battle(caller, monster, BATTLE_MODES.IMMEDIATE_FIGHT)
                        if not monster.is_on_board:
                            del self.monsters[i]
                        return True
                # hero -> npc
                for i, one_npc in enumerate(self.npc):
                    if one_npc.position_x == positionX and one_npc.position_y == positionY:
                        if one_npc.on_meet(self.hero):  # return True if hero start fight with NPC else False
                            if not one_npc.is_on_board:
                                del self.npc[i]
                                return True
                        return False

            elif issubclass(type(caller), Monster):
                # monster -> hero
                if self.pos_x == positionX and self.pos_y == positionY:
                    cprint(f'{self.hero.name} has been attacked by {caller.name}!', ERROR, start_enter=1, wait_after=1)
                    battle(self.hero, caller, BATTLE_MODES.IMMEDIATE_FIGHT)
                    self.monsters.remove(caller)    # Not sure if this will work with many monsters
                    return True

                # monster -> npc
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

                else:
                    new_x_pos, new_y_pos = self.hero.move(key_pressed)  # he

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
                if field.symbol_on_map == '0':
                    middle_fileds += BG_COLOR.GREEN + ' ' + STYLES.RESET
                else:
                    middle_fileds += BG_COLOR.GREEN + field.color_on_board + field.symbol_on_map + STYLES.RESET

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
