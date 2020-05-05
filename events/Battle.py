import time
from utils.decorations import cprint
from utils.validation import int_input
from macros import BATTLE_MODES
from macros.COLORS import *
from utils.utils import clear_screen
from classes.Object.Creature.Hero.Hero_Breed.Sorcerer import Sorcerer

from utils.sounds import *


# from pygame.mixer import music
# from pygame.mixer import Sound

def battle(hero, monster, battle_mode=BATTLE_MODES.MANUAL_FIGHT, hero_start=True):
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


    def battle_image():
        with open("events/battle.txt", "r") as f:
            for row in f:
                cprint((row[:-1]), COLOR.RED, STYLES.BOLD)

    def calculate_dmg(v2, v3):
        if v2 == 'magic':
            return hero.magic_dmg * v3
        elif v2 == 'physical':
            return hero.phys_dmg * v3
        elif v2 == 'magic_and_physical':
            return hero.magic_dmg * hero.phys_dmg * v3
        elif v2 == 'energy_and_stamina':
            return (hero.energy * hero.stamina) / 2

    def hero_move():

        if battle_mode == BATTLE_MODES.MANUAL_FIGHT:
            valid = True
            while valid:
                spell_name_print = ''
                max_key = 2
                for k, v in hero.spells.items():
                    if k is 9:
                        spell_name_print += f"{' ' * 8}[{k}] HP Potions | MANA Potions \n{' ' * 12}H:{hero.hp} {' ' * 6}B: {hero.mana}"
                    else:
                        if hero.energy >= v[4]:
                            max_key += 1
                            skill = calculate_dmg(v[2], v[3])
                            spell_name_print += f"{' ' * 8}[{k}] {v[0]} [dmg:{int(skill)}] (mana cost:{v[1]})\n"

                spell_name_print += '\nWhat should I do master?: '
                hero_attack = int_input(spell_name_print, number_of_options=max_key)
                spell_mana_cost = hero.spells[hero_attack][1]
                wait(1)

                # if hero_attack == '9':
                #     print("You have pressed number 999")
                #     time.sleep(1)

                if spell_mana_cost >= hero.mana:
                    print(f"You dont have enough mana ({hero.mana}) to use this spell.")
                    time.sleep(1)
                    valid = True
                else:
                    hero.mana -= spell_mana_cost
                    valid = False

            calc_dmg = calculate_dmg(hero.spells[hero_attack][2], hero.spells[hero_attack][3])
            hero.attack(monster, calc_dmg)
            # attack = Sound('db/sounds/battle/sword_attack.wav')
            # attack.play()

    # music.pause()
    # music.load('db/sounds/battle.mp3')
    # music.play(-1)

    # Battle start messages
    if hero_start:
        clear_screen()
        battle_image()
        time.sleep(1.5)
        clear_screen()

        cprint(f"You attacked {monster.name}!", ERROR, start_enter=1, wait_after=1)
        who_start = True
    else:
        clear_screen()
        battle_image()
        time.sleep(1.5)
        clear_screen()

        cprint(f'{hero.name} has been attacked by {monster.name}!', ERROR, start_enter=1, wait_after=1)
        who_start = False

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
        if who_start:
            hero_move()
            who_start = False
        # else:
        #     monster.attack(hero, monster.strength)
        #     who_start = True

        if monster.is_alive():
            monster.print_hp()
            wait(1)
            monster.attack(hero, monster.strength)
            hero.print_hp()
            hero.print_mana()
            who_start = True
            wait(1)
        else:
            monster.print_hp()
            wait(1)
            monster.on_defeat()
            break

        if not hero.is_alive():
            hero.print_hp()
            print("FUNCTION ENDING GAME")
            return True

    # Battle end
    cprint(f'You have got {monster.exp} exp.', SUCCESS)
    # music.load('db/sounds/battle/win_battle.mp3')
    # music.play()
    input("\nPress enter to exit fight report...\n")
    # music.stop()
    # music.unpause()
    hero.get_exp(monster.exp)
    hero.add_to_message_box(f"Glorious victory! {monster.name} has been vanquished!")

    # hero.add_items(monster.loot) TODO: to implement
    # return play_music("db/sounds/main_menu_start.mp3", infinite=True)
    # Item.add_to_inventory(hero, monster)
    pass
