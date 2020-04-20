from macros import OBJECT_TYPES, BATTLE_MODES
from classes.Object.Creature.Monster.Monsters import *
from utils import key_service
from macros.COLORS import *
from events.Battle import battle
from classes.Board.Fields import *
from classes.Object.Creature.NPC.NPC import NPC
# from classes.Board.Map_Draw.test_draw import get_background_color
import time


# print('tutaj dzialam', get_background_color('classes/Board/Map_Draw/level1_map.txt'))
class Board:
    def __init__(self, width, height, hero):
        self.width = width
        self.height = height
        #hero
        self.hero = hero
        self.player_sign = hero.symbol_on_map
        self.pos_x = hero.position_x
        self.pos_y = hero.position_y
        #--------------------------------
        self.game_board_in_class = [[self.hero]] + get_background_color('classes/Board/Map_Draw/level1_map.txt') + [[Field()]]
        # print(self.game_board_in_class)
        # print([[hero]] + get_background_color('classes/Board/Map_Draw/level1_map.txt') + [[Field()]])
            # [[self.player_sign]] + [[Field()] * self.width for i in range(self.height)] + [[Field()]]
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero

    # filling = get_background_color('classes/Board/Map_Draw/level1_map.txt')

    monsters = [Troll('Wojtek', 'W', 2, 2), Arnold('Pati', 'P', 4, 4)]
    npc = [NPC('Guard', 'S', 4, 0)]

    def update_board(self):
        self.make_empty_list()
        self.add_object_to_board(self.monsters)
        self.add_object_to_board(self.npc)
        self.game_board_in_class[self.pos_x][self.pos_y] = self.hero
    
    def move_monsters(self):
        
        for monster in self.monsters:
            valid = False
            while not valid:
                x, y = monster.move()
                if self.check_move_possibility(monster, x, y):
                    monster.position_x = x
                    monster.position_y = y
                    valid = True
            
    # def fill_field_with_background(self):
        # for fill in filling:
        # print(self.filling)
    def make_empty_list(self):
        self.game_board_in_class = [[Field()]] + get_background_color('classes/Board/Map_Draw/level1_map.txt') + [[Field()]]
        # self.fill_field_with_background()

    def add_object_to_board(self, object_items):
        for item in object_items:
            self.game_board_in_class[item.position_x][item.position_y] = item

    def check_move_possibility(self, caller, positionX, positionY):
        # Idea for making one for for checking everything instead for loops do it by checking proper value in given caller

        if positionX < 1 or positionY < 0 or positionX > self.width-1:
            return False
        elif self.game_board_in_class[positionX][positionY].field_move_possible == False:
            return False
        else:
            if caller.type_of == OBJECT_TYPES.HERO:

                for i, monster in enumerate(self.monsters):
                    if monster.position_x == positionX and monster.position_y == positionY:

                        battle(caller, monster, BATTLE_MODES.IMMEDIATE_FIGHT)
                        if not monster.is_on_board:
                            del self.monsters[i]
                        return True
                for i, one_npc in enumerate(self.npc):
                    if one_npc.position_x == positionX and one_npc.position_y == positionY:
                        one_npc.on_meet(self.hero)
                        # battle(caller, npc, BATTLE_MODES.IMMEDIATE_FIGHT)
                        # if not monster.is_on_board:
                        #     del self.monsters[i]
                        return True
            elif caller.type_of == OBJECT_TYPES.MONSTER:
                if self.pos_x == positionX and self.pos_y == positionY:
                    battle(self.hero, caller, BATTLE_MODES.IMMEDIATE_FIGHT)

            # monster vs npc validation
            # item in the feature(monster i hero)
            return True



    def get_user_choice(self):
        valid_key = False
        while not valid_key:
            key_pressed = key_service.key_pressed()
            if key_pressed in ['w', 's', 'a', 'd', 'p']:
                if key_pressed == 'p':
                    exit(0)
                else:
                    if key_pressed == 'd':
                        y_y = self.pos_y + 1
                        if self.pos_x == 0 and self.pos_y == 0:
                            self.pos_x += 1
                            valid_key = True
                        
                        elif self.check_move_possibility(self.hero, y_y, self.pos_x):
                            
                            self.pos_y = y_y
                            valid_key = True

                    elif key_pressed == 'w':
                        x_x = self.pos_x - 1
                        if self.check_move_possibility(self.hero, x_x, self.pos_y):
                            valid_key = True
                            self.pos_x = x_x
                        
                    elif key_pressed == 'a':
                        y_y = self.pos_y - 1
                        if self.check_move_possibility(self.hero, self.pos_x, y_y):
                            valid_key = True
                            self.pos_y = y_y

                    elif key_pressed == 's':
                        x_x = self.pos_x + 1
                        if self.check_move_possibility(self.hero, x_x, self.pos_y):
                            valid_key = True
                            self.pos_x = x_x


    def print_board(self):
        # overscore = "\u203e"

        # MIDDLE
        for i, list_of_fields in enumerate(self.game_board_in_class):
            if i == 0:
                middle_fileds = f"{' '*5}"
            elif i == 1 or i == self.height+1:
                middle_fileds += ''
            else:
                middle_fileds += f"\n{' '* 6}"
            # print('TUTAJ JESTEM', self.game_board_in_class)
            for field in list_of_fields:
                # print(field)
                # if field.symbol_on_map:
                middle_fileds += field.field_color + ' ' + STYLES.RESET
                # else:
                #     middle_fileds += BG_COLOR.BLUE + field.color_on_board + field.symbol_on_map + STYLES.RESET


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
