from classes.Object.Creature.Creature import Creature
from macros import DIFFICULTY_LEVEL
from macros.COLORS import *
from macros import MOVES_TYPES
from classes.Object.Item.Item import Item


class Monster(Creature):
    color_on_board = COLOR.RED
    color_in_battle = COLOR.RED

    def __init__(self, name="Set_me_name", symbol_on_map="M", position_x=-1, position_y=-1,
                 strength=10,
                 hp=100,
                 max_hp=100,
                 agility=10,
                 luck=10,
                 move_type=MOVES_TYPES.RANDOM,
                 move_param=None,
                 loot=None,
                 exp=50,
                 on_fight_message="You have no chance with me! ",
                 on_die_message="Argghr...",
                 list_of_positions=None,
                 field_color=BG_COLOR.BLUE
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility, luck)

        if list_of_positions is None:
            self.list_of_positions = []
        self.field_color = field_color
        self.move_type = move_type
        self.exp = exp
        if loot is None:
            self.loot = {}
        else:
            self.loot = loot
        self.on_fight_message = on_fight_message
        self.on_die_message = on_die_message
        self.move_param = move_param

    def on_defeat(self):
        cprint(f'{self.name} has been defeated!', ERROR)
        cprint(f'{self.name}: {self.on_die_message}\n', self.color_in_battle)

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)

    @staticmethod
    def difficulty_depends(number, difficulty_level):
        return int(number * difficulty_level)

    # <----------------------------- MONSTERS ------------------------------------>

    @classmethod
    def troll(cls, pos_x, pos_y, dif_lvl=DIFFICULTY_LEVEL.NORMAL):
        dif_dep = cls.difficulty_depends  # shortcut only
        return cls(name="Troll",
                   position_x=pos_x,
                   position_y=pos_y,
                   symbol_on_map="T",
                   strength=dif_dep(40, dif_lvl),
                   max_hp=dif_dep(200, dif_lvl),
                   hp=dif_dep(200, dif_lvl),
                   move_type=MOVES_TYPES.RANDOM,
                   exp=100,
                   loot={
                       "gloves": Item.shield(12),
                       "coins": 100,
                       "key": Item.key()
                   },
                   )

    @classmethod
    def troll_warrior(cls, pos_x, pos_y, dif_lvl=DIFFICULTY_LEVEL.NORMAL):
        dif_dep = cls.difficulty_depends  # shortcut only
        return cls(name="Troll warrior",
                   position_x=pos_x,
                   position_y=pos_y,
                   symbol_on_map="T",
                   strength=dif_dep(50, dif_lvl),
                   max_hp=dif_dep(300, dif_lvl),
                   hp=dif_dep(300, dif_lvl),
                   move_type=MOVES_TYPES.RANDOM_STRAIGHT,
                   exp=150,
                   loot={
                       'coins': 250,
                        "belt": Item.belt(7)
                   },
                   )

    @classmethod
    def giant(cls, pos_x, pos_y, dif_lvl=DIFFICULTY_LEVEL.NORMAL):
        dif_dep = cls.difficulty_depends  # shortcut only
        return cls(name="Giant",
                   position_x=pos_x,
                   position_y=pos_y,
                   symbol_on_map='G',
                   strength=dif_dep(80, dif_lvl),
                   hp=dif_dep(1000, dif_lvl),
                   max_hp=dif_dep(1000, dif_lvl),
                   luck=0,
                   agility=0,
                   move_type=MOVES_TYPES.RANDOM_STRAIGHT,
                   exp=1000,
                   loot={
                       "gloves": Item.gloves(6)
                   },
                   on_fight_message="YOU LITTLE RAT!",
                   on_die_message="I will be back...",
                   )

    @classmethod
    def rat(cls, pos_x, pos_y, dif_lvl=1):
        return cls(name="Rat",
                   position_x=pos_x,
                   position_y=pos_y,
                   move_type=MOVES_TYPES.GUARD_HORIZONTAL,
                   move_param=[3, [0]],
                   symbol_on_map="R",
                   agility=50,
                   loot={
                       "boots": Item.boots(4),
                       "belt": Item.belt(3)
                   },
                   on_fight_message="wee wee wee")

    @classmethod
    def snake(cls, pos_x, pos_y, dif_lvl=DIFFICULTY_LEVEL.NORMAL):
        dif_dep = cls.difficulty_depends  # shortcut only
        return cls(name="Snake",
                   position_x=pos_x,
                   position_y=pos_y,
                   symbol_on_map="S",
                   hp=dif_dep(50, dif_lvl),
                   max_hp=dif_dep(50, dif_lvl),
                   strength=dif_dep(20, dif_lvl),
                   agility=80,
                   luck=30,
                   loot={
                       "key": Item.key(),
                       "gloves": Item.shield(9),

                   },
                   on_fight_message="sssss",
                   on_die_message="sssss",
                   )

    @classmethod
    def finall_boss(cls, pos_x, pos_y, list_of_positions, dif_lvl=DIFFICULTY_LEVEL.HARD):
        dif_dep = cls.difficulty_depends
        return cls(name="Belzedup",
                   field_color=COLOR.RED,
                   position_x=pos_x,
                   position_y=pos_y,
                   list_of_positions=list_of_positions,
                   symbol_on_map='6',
                   strength=dif_dep(100, dif_lvl),
                   hp=dif_dep(1000, dif_lvl),
                   max_hp=dif_dep(1000, dif_lvl),
                   luck=10,
                   agility=20,
                   move_type=MOVES_TYPES.RANDOM_DIAGONAL,
                   exp=10000,
                   loot={
                       "quest_items": Item.quest_item("Order zajebistości")
                   },
                   on_fight_message="You will burn in hell for ever!!",
                   on_die_message="I will be back...",
                   )
