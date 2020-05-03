import time
from utils.decorations import cprint
from utils.validation import int_input
from macros import BATTLE_MODES
from macros.COLORS import *
from classes.Object.Creature.Hero.Hero_Breed.Sorcerer import Sorcerer

from utils.sounds import *
from pygame.mixer import music
from pygame.mixer import Sound
from classes.Object.Item.Item import Item


def battle(hero, monster, battle_mode=BATTLE_MODES.MANUAL_FIGHT):
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
            valid = True
            while valid:
                spell_name_print = ''
                max_key = 2
                for k, v in hero.spells.items():
                    if k is 0:
                        # 0: ['HP potion: ', self.hp, 'MANA potion: ', self.mana]
                        spell_name_print += f"{' '*8}[{k}] HP Potions | MANA Potions \n{' '*12}H:{hero.hp} {' '*6}B: {hero.mana}"
                    else:
                        if hero.energy >= v[4]:
                            max_key += 1
                            spell_name_print += f"{' '* 8}[{k}] {v[0]} (mana cost:{v[1]})\n"

                spell_name_print += '\nWhat should I do master?: '
                hero_attack = int_input(spell_name_print, number_of_options=max_key)
                spell_mana_cost = hero.spells[hero_attack][1]

                if spell_mana_cost >= hero.mana:
                    print(f"You dont have enough mana ({hero.mana}) to use this spell.")
                    time.sleep(1)
                    valid = True
                else:
                    hero.mana -= spell_mana_cost
                    valid = False


            # print(hero.spells.items())
            # time.sleep(10)
            # print(f"You have choiced {spell_name_choice[0]}")
            # time.sleep(1)

            # 0 = Name,
            # 1 = mana cost,
            # 2 = kind of dmg,
            # 3 = dmg_ratio

            calc_dmg = hero.spells[hero_attack][2] * hero.spells[hero_attack][3]
            hero.attack(monster, calc_dmg)
            # attack = Sound('db/sounds/battle/sword_attack.wav')
            # attack.play()

        #
        # else:
        #     hero.attack(monster)



    # Battle start messages
    # music.pause()
    # music.load('db/sounds/battle.mp3')
    # music.play(-1)
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
            monster.attack(hero, monster.strength)
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
    # music.load('db/sounds/battle/win_battle.mp3')
    # music.play()
    input("\nPress enter to exit fight report...\n")
    # music.stop()
    # music.unpause()
    hero.get_exp(monster.exp)

    # hero.add_items(monster.loot) TODO: to implement
    # return play_music("db/sounds/main_menu_start.mp3", infinite=True)
    # Item.add_to_inventory(hero, monster)
    pass

