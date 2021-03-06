from classes.Object.Creature.Hero.Hero import Hero
from macros.COLORS import *
from macros import MOVES_TYPES


class Sorcerer(Hero):
    def __init__(self, name="Set_me_name", symbol_on_map="\u03A8", position_x=0, position_y=0,
                 strength=28,
                 hp=200,
                 max_hp=200,
                 agility=20,
                 phys_dmg=13,
                 luck=3,
                 dodge_chance=3,
                 defense=18,
                 stamina=15,
                 energy=28,
                 magic_dmg=2,
                 mana=100,
                 max_mana=100,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=1,
                 exp=0,
                 exp_to_next_level=100,
                 breed='Sorcerer',
                 spells = {},
                 coins=100
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility,
                         color_in_battle, move_type, level, exp, exp_to_next_level,phys_dmg,
                         luck,dodge_chance,defense,stamina,energy,magic_dmg,mana,max_mana,spells)

        self.phys_dmg += (self.strength*0.5)
        self.luck += (self.agility*0.3)
        self.dodge_chance += (self.agility*0.3)
        self.defense += (self.agility*0.3)
        self.hp += (self.stamina*2)
        self.max_hp += (self.stamina*2)
        self.magic_dmg += (self.energy*3)
        self.mana += (self.energy*2)
        self.max_mana += (self.energy*2)
        self.coins = coins
        self.breed = breed
        self.color_on_board = STYLES.BOLD + COLOR.BLUE
        # extra_atributes per point
        self.stats_ratio = {
            0: 1,
            1: [3, 0.4, 1],
            2: 6,
            3: [3, 5]
        }

        # 0 = Name, 1 = mana cost, 2 = kind of dmg, 3 = dmg_ratio, 4 = energy required
        self.spells = {
            1: ['Physical damage', 0, 'physical', 1, 1],
            2: ['Fire Ball', 10, 'magic', 1, 24],
            3: ['Aqua Beam',  20, 'magic', 1.1, 38],
            4: ['Fire storm', 50, 'magic', 1.2, 48],
            5: ['Decay', 80, 'magic', 1.5, 60],
            6: ['Ice Storm', 100, 'magic', 1.7, 66],
            7: ['Inferno', 150, 'magic', 3, 75],
            # 8: ['Block and heal', 40, 'energy_and_stamina', 1, 50],
            9: ['HP potion: ', self.hp, 'MANA potion: ', self.mana]
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

    # def spell_fire_ball(self):
    #     self.mana -= 30
    #     name = 'Fire Ball'
    #     dmg_from_spell = 3 * self.magic_dmg
    #
    #
    # def spell_aqua_beam(self):
    #     self.mana -= 50
    #     name = 'Aqua Beam'
    #     dmg_from_spell = 5 * self.magic_dmg









