class Board:
    def __init__(self, width, height, p_sign):
        self.width = width
        self.height = height
        self.pos_x = -1
        self.pos_y = -1
        self.player_sign = p_sign

    def create_board(self): # this maybe can go to the __init__
        self.game_board_in_class = [['0'] * self.width for i in range(self.height)]
        # self.game_board_in_class = [['0'] * self.width if i != 0 or i != self.height else ['0'] * (self.width+1) 
        #                             for i in range(self.height)]
        


    def update_board(self, pos_x, pos_y):
        self.game_board_in_class[pos_x][pos_y] = self.player_sign
        self.pos_x = pos_x
        self.pos_y = pos_y
        # self.game_board_in_class[x][y] = sign_on_map
       

    def remove_player_track(self):
        # print(type(self.pos_x))
        self.game_board_in_class[self.pos_x][self.pos_y] = '0'


    def print_board(self):
        overscore = "\u203e"
        # TOP

        letters_position = f"{' '*15}"
        for item in range(len(self.game_board_in_class)):
            letters_position += chr(65 + item % 26) + ' '*2
        print('\n', letters_position + '\n', f"{' '*11}{'_'*(self.width*3+3)}", sep='')
        # MIDDLE
        middle_fileds = ''
        for i, list_of_fields in enumerate(self.game_board_in_class):
            if i == 0:
                middle_fileds += f"{' '*6}{i+1}.{' '*3}|{self.player_sign}|"
            elif i == 1:
                middle_fileds += f"{' '*6}{i+1}.{' '*3} {overscore}|"
            else:
                middle_fileds += f"{' '* (7 - len(str(i+1)))}{i+1}.{' ' * 5}|"
            
            for field in list_of_fields:
                if field == '0':
                    middle_fileds += '   '
                else:
                    middle_fileds = middle_fileds + ' ' + field + ' '
         
            if i == len(self.game_board_in_class)-2:
                middle_fileds += '|_\n'
            elif i == len(self.game_board_in_class)-1:
                middle_fileds += '| |'
            else:
                middle_fileds += '|\n'

        print(middle_fileds, sep='')
        # self.bo


        # BOTTOM

        print(f"{' '*14}{overscore*(self.width*3+3)}\n")
