import time
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monsters import Troll, Arnold
from utils.decorations import cprint
from macros import BATTLE_MODES
from macros.COLORS import *


def battle(hero, monster, battle_mode=BATTLE_MODES.AUTOMATE_FIGHT):
    """

    :param hero:[object]
    :param monster:[object]
    :param battle_mode:[string]:[IMMEDIATE_FIGHT, AUTOMATE_FIGHT, MANUAL_FIGHT]
    :return: pass
    """

    def wait(wait_time):
        """
        :param wait_time:[float] amount of time to wait in seconds
        :return: pass
        """
        if battle_mode == BATTLE_MODES.AUTOMATE_FIGHT:
            time.sleep(wait_time)

    def hero_move():
        if battle_mode == BATTLE_MODES.MANUAL_FIGHT:
            hero_attack = None
            while hero_attack not in [1, 2]:
                hero_attack = int(input('[1] Attack \n'
                                        '[2] Special Attack \n'
                                        'What should I do master?: '))
                if hero_attack == 1:
                    hero.attack(monster)
                elif hero_attack == 2:
                    hero.special_attack(monster)
        else:
            hero.attack(monster)

    # Battle start messages
    cprint(f"\nBattle start! {hero.name} vs {monster.name}\n", COLOR.PURPLE)
    hero.start_fight_message()
    monster.start_fight_message()
    print("")   # \n

    # Battle
    round_counter = 0
    while monster.is_alive():
        wait(1)
        round_counter += 1
        cprint(f"Round: {round_counter}", COLOR.PURPLE)
        wait(1)

        hero_move()

        if monster.is_alive():
            monster.print_hp()
            wait(1)
            monster.attack(hero)
            hero.print_hp()
            wait(1)
        else:
            monster.print_hp()
            wait(1)
            monster.on_defeat()

        if not hero.is_alive():
            hero.print_hp()
            print("FUNCTION ENDING GAME")
            break

    # Battle end
    hero.get_exp(monster.exp)
    # hero.add_items(monster.loot) TODO: to implement
    input("\nPress any button to exit fight report...")
    pass


# hero = Hero("Andrzej", "X", 1, 1)
# Arnold1 = Arnold("Arni", "O", 1, 1)
# battle(hero, Arnold1, BATTLE_MODES.IMMEDIATE_FIGHT)

