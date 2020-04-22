
from classes.Object.Object import MyObject
from macros import COLORS

class Field():
    symbol_on_map = '0'
    field_color = COLORS.BG_COLOR.GREEN
    field_move_possible = True

class Wall():
    symbol_on_map = '-'
    field_color = COLORS.BG_COLOR.LIGHTGREY
    field_move_possible = False

map_file = 'classes/Board/Map_drawing/level1_map.txt'
# map_file2 = 'class'

def get_background_color(map_file_name=map_file):
    with open(map_file_name, 'r') as f:
        full_map = f.readlines()
        full_map_list = [list(item.strip()) for item in full_map]
        # print(full_map_list)
        list_of_all_fields = []
        for row in full_map_list:
            row_of_fields = []
            for i, elem in enumerate(row):
                if elem == '0':
                    row_of_fields.append(Field())
                elif elem == '-':
                    row_of_fields.append(Wall())
            list_of_all_fields.append(row_of_fields)
        # print(full_map_list)
    return list_of_all_fields
# map_list = get_background_color(map_file)
# print(map_list)