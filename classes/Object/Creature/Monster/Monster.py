from classes.Object.Creature.Creature import Creature
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *
from macros import MOVES_TYPES


class Monster(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="M", position_x=-1, position_y=-1,
                 strength=10,
                 hp=100,
                 max_hp=100,
                 agility=10,
                 luck=10,
                 color_in_battle=COLOR.RED,
                 move_type=MOVES_TYPES.RANDOM,
                 color_on_board=COLOR.RED,
                 exp=50,
                 loot=None,
                 field_color=BG_COLOR.BLUE,
                 field_move_possible=True,
                 on_fight_message="You have no chance with me! ",
                 on_die_message="Argghr..."
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility, luck)

        self.color_in_battle = color_in_battle
        self.color_on_board = color_on_board
        self.move_type = move_type
        self.exp = exp
        if loot is None:
            self.loot = {}
        self.field_color = field_color
        self.field_move_possible = field_move_possible
        self.on_fight_message = on_fight_message
        self.on_die_message = on_die_message

    type_of = OBJECT_TYPES.MONSTER  # probably to delete

    def on_defeat(self):
        cprint(f'{self.name} has been defeated!', ERROR)
        cprint(f'{self.name}: {self.on_die_message}\n', self.color_in_battle)

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)
