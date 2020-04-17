from macros import OBJECT_TYPES, BATTLE_MODES
from classes.Object.Creature.Monster.Monsters import *
from utils import key_service
from events.Battle import battle


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
        self.game_board_in_class = [[self.player_sign]] + [['0'] * self.width for i in range(self.height)] + [['0']]
        self.game_board_in_class[self.pos_x][self.pos_y] = self.player_sign


    monsters = [Troll('Wojtek', 'W', 2, 2), Arnold('Pati', 'P', 4, 4)]

    def update_board(self):
        self.add_monster_to_board()
        self.game_board_in_class[self.pos_x][self.pos_y] = self.player_sign
    
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
        self.game_board_in_class = [[self.player_sign]] + [['0'] * self.width for i in range(self.height)] + [['0']]
        for i, monster in enumerate(self.monsters):
            if not monster.is_on_board:
                del self.monsters[i]
      
        self.update_board()

    def add_monster_to_board(self):
        for monster in self.monsters:
            self.game_board_in_class[monster.position_x][monster.position_y] = monster.symbol_on_map

    def check_move_possibility(self, caller, positionX, positionY):
        # position is where i want to move:
        # caller is monster/Hero who call this function

        # caller.type = "Monster"
        # return False if monster, item or wall
        # start fight if Hero, return True
        # else True
        # if caller.type_of == OBJECT_TYPES.MONSTER:


        # caller.type = "Hero"
        # return False if wall
        # start fight if monster, return True
        # add item to Hero inventory if item, return True
        # else True

        if caller.type_of == OBJECT_TYPES.HERO:
            for monster in self.monsters:
                if monster.position_x == positionX and monster.position_y == positionY:
                    battle(caller, monster, BATTLE_MODES.IMMEDIATE_FIGHT)
                    return True
        # print(self.pos_x, self.pos_y)
        if positionX < 1 or positionY < 0:
            return False
        else:
            return True
        # return True

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
                            # self.check_move_possibility(self.hero, y_y, self.pos_y)
                            self.pos_x += 1
                        
                        elif self.check_move_possibility(self.hero, y_y, self.pos_y):
                            valid_key = True
                            self.pos_y = y_y

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


    def remove_player_track(self):
        # print(type(self.pos_x))
        self.game_board_in_class[self.pos_x][self.pos_y] = '0'


    def print_board(self):
        overscore = "\u203e"
        print(self.game_board_in_class)
        # TOP

        letters_position = f"{' '*14}"
        for item in range(self.width):
            letters_position += chr(65 + item % 26)
        print('\n', letters_position + '\n', f"{' '*12}{'_'*(self.width+3)}", sep='')

        # MIDDLE
        for i, list_of_fields in enumerate(self.game_board_in_class):
            if i == 0:
                middle_fileds = f"{' '*6}{1}.{' '*5}"
            elif i == 1:
                middle_fileds += ''
            elif i == 2:
                middle_fileds += f"\n{' '*6}{i}.{' '*4}{overscore}|"

            elif i == len(self.game_board_in_class)-1:
                middle_fileds += ''
            else:
                middle_fileds += f"{' '* (7 - len(str(i)))}{i}.{' ' * 5}|"
            
            for field in list_of_fields:

                if field == '0':
                    middle_fileds += ' '
                else:
                    middle_fileds += field
            
            if i == 0:
                middle_fileds += ''
            elif i == 1:
                middle_fileds += '|'
            elif i == len(self.game_board_in_class)-3:
                middle_fileds += '|_\n'
            elif i == len(self.game_board_in_class)-2:
                middle_fileds += ''
            elif i == len(self.game_board_in_class)-1:
                middle_fileds += ''

            else:
                middle_fileds += '|\n'

        print(middle_fileds, sep='')

        # BOTTOM
        print(f"{' '*13}{overscore*(self.width+3)}\n")
