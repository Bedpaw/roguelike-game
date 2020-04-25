import time
from utils.decorations import cprint
from utils.validation import int_input
from macros import BATTLE_MODES
from macros.COLORS import *
from classes.Object.Item.Item import Item


def battle(hero, monster, battle_mode=BATTLE_MODES.IMMEDIATE_FIGHT):
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
            hero_attack = int_input('[1] Attack \n'
                                    '[2] Special Attack \n'
                                    'What should I do master?: ', number_of_options=2)
            if hero_attack == 1:
                hero.attack(monster)
            elif hero_attack == 2:
                hero.special_attack(monster)
        else:
            hero.attack(monster)

    # Battle start messages
    cprint(f"Battle start! {hero.name} vs {monster.name}", COLOR.PURPLE, start_enter=1, end_enter=1)
    hero.start_fight_message()
    monster.start_fight_message()

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
    cprint(f'You have got {monster.exp} exp.', SUCCESS)
    input("\nPress enter to exit fight report...\n")
    hero.get_exp(monster.exp)
    Item.add_to_inventory(monster.loot)
    pass