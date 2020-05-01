from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import COLOR
from macros import MOVES_TYPES, OBJECT_TYPES


class Sorcerer(Hero):
    def __init__(self, name="Set_me_name", symbol_on_map="K", position_x=0, position_y=0,
                 strength=28,
                 hp=500,
                 max_hp=500,
                 agility=20,
                 phys_dmg=13,
                 luck=3,
                 dodge_chance=3,
                 defense=8,
                 stamina=25,
                 energy=10,
                 magic_dmg=2,
                 mana=50,
                 max_mana=50,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Sorcerer'

                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility,
                         color_in_battle, move_type, level, exp, exp_to_next_level,phys_dmg,
                         luck,dodge_chance,defense,stamina,energy,magic_dmg,mana,max_mana,)

        self.phys_dmg += (self.strength*0.5)
        self.luck += (self.agility*0.3)
        self.dodge_chance += (self.agility*0.3)
        self.defense += (self.agility*0.3)
        self.hp += (self.stamina*2)
        self.max_hp += (self.stamina*2)
        self.magic_dmg += (self.energy*2)
        self.mana += (self.energy*2)
        self.max_mana += (self.energy*2)

        self.breed = breed

        # extra_atributes per point
        self.stats_ratio = {
            0: 1,
            1: [3, 2, 1],
            2: 6,
            3: [2, 5]
        }

        # level up attributes
    def level_up_attributes(self):
        self.phys_dmg += 0.5
        self.luck += 1
        self.dodge_chance += 2
        self.defense += 1
        self.hp += 3
        self.max_hp += 3
        self.magic_dmg += 3
        self.mana += 5
        self.max_mana += 5





