from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import COLOR
from macros import MOVES_TYPES, OBJECT_TYPES



class Knight(Hero):
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
                 energy=50,
                 magic_dmg=2,
                 mana=50,
                 max_mana=50,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Knight',
                 spells={}
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility,
                         color_in_battle, move_type, level, exp, exp_to_next_level,phys_dmg,
                         luck,dodge_chance,defense,stamina,energy,magic_dmg,mana,max_mana,spells)

        self.phys_dmg += (self.strength*1)
        self.luck += (self.agility*0.2)
        self.dodge_chance += (self.agility*0.2)
        self.defense += (self.agility*0.5)
        self.hp += (self.stamina*3)
        self.max_hp += (self.stamina*3)
        self.magic_dmg += (self.energy*0.1)
        self.mana += (self.energy*0.2)
        self.max_mana += (self.energy*0.2)

        self.breed = breed

        # extra_atributes per point
        self.stats_ratio = {
            0: 2,
            1: [1, 0.1, 3],
            2: 10,
            3: [1, 2]
        }
        self.spells = {
            1: ['Physical damage', 0, 'physical', 1.5, 1],
            2: ['Cyclon Cutting', 7, 'physical', 2, 10],
            3: ['Twisting Slash', 12, 'physical', 2.5, 15],
            4: ['Regular Blow',  15, 'physical', 3, 20],
            5: ['Death Stab',  20, 'physical', 8, 40],
            6: ['Barrier (+100 defense)', 50, 'energy_and_stamina', 2, 50],
            9: ['HP potion: ', self.hp, 'MANA potion: ', self.mana]
        }

        # level up attributes
    def level_up_attributes(self):
        self.phys_dmg += 3
        self.luck += 1
        self.dodge_chance += 1
        self.defense += 3
        self.hp += 5
        self.max_hp +=5
        self.magic_dmg += 0.1
        self.mana += 1
        self.max_mana += 1





