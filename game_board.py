class Board:
    def __init__(self, width, height, p_sign):
        self.width = width
        self.height = height
        self.player_sign = p_sign
        self.game_board_in_class = [[self.player_sign]] + [['0'] * self.width for i in range(self.height)] + [['0']]
        self.game_board_in_class[self.pos_x][self.pos_y] = self.player_sign
        
    pos_x = 0
    pos_y = 0


    def update_board(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.game_board_in_class[pos_x][pos_y] = self.player_sign


       

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
                middle_fileds = f"{' '*6}{1}.{' '*4}|"
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
