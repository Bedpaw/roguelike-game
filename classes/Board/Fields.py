
from classes.Object.Object import MyObject
from macros import COLORS


class Gate():
    symbol_on_map = ' '
    color_on_board = COLORS.COLOR.RED
    field_color = COLORS.BG_COLOR.GREEN
    field_move_possible = True


class Field():
    symbol_on_map = '0'
    color_on_board = ''
    field_color = COLORS.BG_COLOR.GREEN
    field_move_possible = True


class Wall_Horizontal():
    symbol_on_map = '-'
    color_on_board = ''
    field_color = COLORS.BG_COLOR.LIGHTGREY
    field_move_possible = False
    on_move_message = "You hit a wall!"


class River():
    symbol_on_map = '~'
    color_on_board = COLORS.COLOR.BLUE
    field_color = COLORS.BG_COLOR.BLUE
    field_move_possible = False
    on_move_message = "This water is too deep!"


class Bridge():
    symbol_on_map = '='
    color_on_board = COLORS.COLOR.BROWN
    field_color = COLORS.BG_COLOR.CYAN
    field_move_possible = True


class Wall_Vertical():
    symbol_on_map = '|'
    color_on_board = ''
    field_color = COLORS.BG_COLOR.LIGHTGREY
    field_move_possible = False
    on_move_message = "You hit a wall!"


class Fire():
    # symbol_on_map = "\u03A8"
    symbol_on_map = "^"
    color_on_board = COLORS.COLOR.RED
    field_color = COLORS.BG_COLOR.ORANGE
    field_move_possible = True
    on_move_message = "You have step on lava -20 hp!"

class Lava_pavement():
    symbol_on_map = "#"
    field_color = COLORS.BG_COLOR.LIGHTGREY
    color_on_board = COLORS.COLOR.RED
    field_move_possible = True

class Tree_Left():
    symbol_on_map = "]"
    field_color = COLORS.BG_COLOR.GREEN
    color_on_board = COLORS.COLOR.DARKGREEN
    field_move_possible = True

class Tree_Right():
    symbol_on_map = "["
    field_color = COLORS.BG_COLOR.GREEN
    color_on_board = COLORS.COLOR.DARKGREEN
    field_move_possible = True


map_file = 'classes/Board/Map_drawing/level1_map.txt' # :TODO REMOVE?

symbols_to_txt_draw = {
    '0': Field(),
    '-': Wall_Vertical(),
    '~': River(),
    '=': Bridge(),
    ' ': Gate(),
    '|': Wall_Horizontal(),
    'v': Fire(),
    "#": Lava_pavement(),
    "]": Tree_Left(),
    "[": Tree_Right(),
}

def get_map(map_file_name=map_file):
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
    return list_of_all_fields
