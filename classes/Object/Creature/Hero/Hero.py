from classes.Object.Creature.Creature import Creature
from macros.COLORS import *
from utils.decorations import cprint, ctext
from macros import MOVES_TYPES, OBJECT_TYPES
from utils.key_service import *

class Hero(Creature):
    def __init__(self, name="Set_me_name", symbol_on_map="@", position_x=-1, position_y=-1,
                 strength=0,
                 hp=0,
                 max_hp=0,
                 agility=0,
                 color_in_battle=COLOR.GREEN,
                 move_type=MOVES_TYPES.MANUAL,
                 level=0,
                 exp=0,
                 exp_to_next_level=0,
                 phys_dmg=0,
                 luck=0,
                 doge_chance=0,
                 defense=0,
                 stamina=0,
                 energy=0,
                 magic_dmg=0,
                 mana=0,
                 max_mana=0,
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility)
        self.color_in_battle = color_in_battle
        self.move_type = move_type
        self.level = level
        self.points_for_level = 0
        self.exp = exp
        self.exp_to_next_level = exp_to_next_level
        self.phys_dmg = phys_dmg
        self.luck = luck
        self.doge_chance = doge_chance
        self.defense = defense
        self.stamina = stamina
        self.energy = energy
        self.magic_dmg = magic_dmg
        self.mana = mana
        self.max_mana = max_mana
        self.breed = 'Knight'

    type_of = OBJECT_TYPES.HERO
    color_on_board = STYLES.BOLD + COLOR.CBLACK


    inventory = {
        "coins": 100,
    }
    on_fight_message = "Time to stop this creature!"
    def level_up(self):
        """
        1) Add level
        2) Set new exp_to_next_level
        3) Improve hero skills
        :return: pass
        """
        self.level += 1
        self.points_for_level += 5
        self.exp_to_next_level = self.exp + int(self.exp_to_next_level * 1.3)
        cprint(f"You have received {self.level} level!", SUCCESS)
        stats = self.stats_info()
        # TODO
        # REGEX in future
        indexes = [1, 3, 7, 9]
        for i, item in enumerate(stats):
            if i in indexes:
                item[i] += ' + | -'

        while key_pressed() != 'l':

            print('\n'.join(stats))



    def get_exp(self, exp):
        """
        Add exp and check if lvl up
        :param exp:[int]: exp to add for hero
        :return: pass
        """
        exp_to_next_level = self.exp_to_next_level - self.exp
        if exp >= exp_to_next_level:
            exp -= exp_to_next_level
            self.level_up()
            self.get_exp(exp)
        else:
            self.exp += exp
        pass

    def start_fight_message(self):
        cprint(f'{self.name}: {self.on_fight_message}', self.color_in_battle)

    def special_attack(self, target):
        """
        Instant kill enemy [only for test]
        :param target:[object] enemy to kill
        :return: pass
        """
        target.hp = 0
        cprint(f'{self.name} is stupid cheater...', self.color_in_battle)

    def stats_info(self):
        return[f"{' '*5}Skill points: {self.points_for_level}",
            f"{' '*5}{BG_COLOR.RED}{COLOR.CBLACK}{STYLES.BOLD}    strength:     {self.strength}{STYLES.RESET}",
            f"{' '*5}  (physical dmg: {self.phys_dmg})",
            f"{' '*5}{BG_COLOR.GREEN}{COLOR.CBLACK}{STYLES.BOLD}    agility:      {self.agility}{STYLES.RESET}",
            f"{' '*5}  (crit_chance:  {self.luck})",
            f"{' '*5}  (doge chance:  {self.doge_chance})",
            f"{' '*5}  (defense:      {self.defense})",
            f"{' '*5}{BG_COLOR.ORANGE}{COLOR.CBLACK}{STYLES.BOLD}    stamina:      {self.strength}{STYLES.RESET}",
            f"{' '*5}  (hp:   {self.strength})",
            f"{' '*5}{BG_COLOR.BLUE}{COLOR.CBLACK}{STYLES.BOLD}    energy:       {self.strength}{STYLES.RESET}",
            f"{' '*5}  (magic dmg:  {self.magic_dmg})",
            f"{' '*5}  (max_mana:  {self.max_mana})"]



