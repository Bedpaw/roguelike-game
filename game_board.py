class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_board(self):
        self.game_board = [['0']*self.width] * self.height
        self.player = 'X'
        # print(self.game_board)

    def print_board(self):
        overscore = "\u203e"
        # TOP

        letters_position = f"{' '*15}"
        for item in range(len(self.game_board)):
            letters_position += chr(65+item%26) + ' '*2
        print('\n', letters_position + '\n', f"{' '*11}{'_'*(self.width*3+3)}", sep='')
        # MIDDLE
        middle_fileds = ''
        for i, list_of_fields in enumerate(self.game_board):
            if i == 0:
                middle_fileds += f"{' '*6}{i+1}.{' '*3}|{self.player}|"
            elif i == 1:
                middle_fileds += f"{' '*6}{i+1}.{' '*3} {overscore}|"
            else:
                middle_fileds += f"{' '* (7 - len(str(i+1)))}{i+1}.{' ' * 5}|"
            
            for field in list_of_fields:
                if field == '0':
                    middle_fileds += '   '
                else:
                    middle_fileds += field
         

            if i == len(self.game_board)-2:
                middle_fileds += '|_\n'
            elif i == len(self.game_board)-1:
                middle_fileds += '| |'
            else:
                middle_fileds += '|\n'

        print(middle_fileds, sep='')


        # BOTTOM

        print(f"{' '*14}{overscore*(self.width*3+3)}\n")
