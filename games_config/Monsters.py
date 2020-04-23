# from classes.Object.Creature.Monster.Monster import Monster
# from macros import MOVES_TYPES, DIFFICULTY_LEVEL
#
#
# #:TODO REFACOTOR TO FUNCTIONS OR ALL MONTERS WILL BE THE SAME OBJECT
#
#
# class Monsters_fabric:
#     def __init__(self, difficulty_level):
#         self.difficulty_level = difficulty_level
#     monster = Monster()
#
#     def TROLL(self):
#         return Monster(
#             name='Troll',
#             symbol_on_map="T",
#             strength=self.difficulty_depends(40),
#             max_hp=self.difficulty_depends(200),
#             hp=self.difficulty_depends(200),
#             move_type=MOVES_TYPES.RANDOM_DIAGONAL,
#             exp=100,
#             loot={
#                 'coins': 150,
#             },
#         )
#
#     def difficulty_depends(self, number):
#         """
#         Change monster stats depends on game difficulty level
#         :param number:
#         :return:
#         """
#         return int(number * self.difficulty_level)
#
#     def set_position(self, position_x, position_y):
#
#
# GIANT = Monster(
#     name="Giant",
#     symbol_on_map='G',
#     strength=difficulty_depends(80),
#     hp=difficulty_depends(1000),
#     max_hp=difficulty_depends(1000),
#     luck=0,
#     agility=0,
#     move_type=MOVES_TYPES.RANDOM_STRAIGHT,
#     exp=1000,
#     loot={
#         'key': 1,
#     },
#     on_fight_message="YOU LITTLE RAT!",
#     on_die_message="I will be back...",
# )
# RAT = Monster(
#     symbol_on_map="R",
#     agility=50,
#     on_fight_message="*pik*pik*"  #:TODO Jak robi szczur? XD
# )
# SNAKE = Monster(
#     hp=difficulty_depends(50),
#     max_hp=difficulty_depends(50),
#     strength=difficulty_depends(20),
#     agility=80,
#     luck=30,
#     on_fight_message="sssss",
#     on_die_message="sssss",
# )
# SHARK = Monster(
#     hp=difficulty_depends(150),
#     max_hp=difficulty_depends(150),
#     strength=difficulty_depends(60),
# )
