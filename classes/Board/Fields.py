
from classes.Object.Object import MyObject
from macros import COLORS


class Gate():
    symbol_on_map = ' '
    field_color = COLORS.BG_COLOR.GREEN
    field_move_possible = True


class Field():
    symbol_on_map = '0'
    field_color = COLORS.BG_COLOR.GREEN
    field_move_possible = True


class Wall():
    symbol_on_map = '-'
    field_color = COLORS.BG_COLOR.LIGHTGREY
    field_move_possible = False


class River():
    symbol_on_map = '~'
    field_color = COLORS.BG_COLOR.BLUE
    field_move_possible = False


class Bridge():
    symbol_on_map = '='
    field_color = COLORS.BG_COLOR.CYAN
    field_move_possible = True


map_file = 'classes/Board/Map_drawing/level1_map.txt'
# map_file2 = 'class'

symbols_to_txt_draw = {
    '0': Field(),
    '-': Wall(),
    '~': River(),
    '=': Bridge(),
    ' ': Gate()
}

def get_map(map_file_name=map_file): #get map
    with open(map_file_name, 'r') as f:
        full_map = f.readlines()
        full_map_list = [list(item.strip()) for item in full_map]
        list_of_all_fields = []
        for row in full_map_list:
            row_of_fields = []
            for i, elem in enumerate(row):
                if elem in symbols_to_txt_draw:
                    row_of_fields.append(symbols_to_txt_draw[elem])
            list_of_all_fields.append(row_of_fields)
    # print(list_of_all_fields)
    return list_of_all_fields
# map_list = get_background_color(map_file)
# print(map_list)