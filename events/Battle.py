import time
from utils.decorations import cprint
from utils.validation import int_input
from macros import BATTLE_MODES
from macros.COLORS import *
from utils import key_service
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
        # elif v2 == 'energy_and_stamina':
        #     return (hero.energy * hero.stamina)/2

    def block_skill_counter():
        pass

    def use_potions():
        key_pressed = key_service.key_pressed()
        if key_pressed.lower() == 'h':
            hero.use_hpotion()
        elif key_pressed.lower() == 'j':
            hero.use_mana()

    def how_many_potions(kind_of_potion):
        counter = 0
        for potion in hero.backpack:
            if potion.item_type == kind_of_potion:
                counter += 1
        return counter

    def hero_move():

        if battle_mode == BATTLE_MODES.MANUAL_FIGHT:
            valid = True
            while valid:
                spell_name_print = ''
                max_key = 2
                for k, v in hero.spells.items():
                    if k is 9:
                        spell_name_print += f"{' '*8}[{k}]{' '*2}Hero HP:{hero.hp}{' '*4}| {' '*2}Hero Mana: {hero.mana}\n"
                        spell_name_print += f"{' '*11}{'-' *40}\n"
                        spell_name_print += f"{' '*20}HP Potions |  MANA Potions \n"
                        spell_name_print += f"{' '*4}[key:qunatity]  H:{how_many_potions('healing_potion')}{' '*11}M: {how_many_potions('mana')}"
                    else:
                        if hero.energy >= v[4]:
                            if v[2] == 'energy_and_stamina':
                                spell_name_print += f"{' ' * 8}[{k}] {v[0]} (mana cost:{v[1]})\n"
                            else:
                                skill = calculate_dmg(v[2], v[3])
                                spell_name_print += f"{' '* 8}[{k}] {v[0]} [dmg:{int(skill)}] (mana cost:{v[1]})\n"
                            max_key += 1

                spell_name_print += '\nWhat should I do master?: '
                max_key_options = [item for item in range(1, max_key)]
                max_key_options += [9]

                hero_attack = int_input(spell_name_print, '', options=max_key_options)
                if hero_attack == 9:
                    use_potions()
                    continue
                else:
                    spell_mana_cost = hero.spells[hero_attack][1]
                    wait(1)

                    if spell_mana_cost >= hero.mana:
                        print(f"You dont have enough mana ({hero.mana}) to use this spell.")
                        time.sleep(1)
                        valid = True
                    else:
                        hero.mana -= spell_mana_cost
                        valid = False

                # protect against use second time ........ TODO
                if hero.spells[hero_attack][2] == 'energy_and_stamina':
                    # hero.special_buff_dmg = calc_dmg
                    hero.special_buff(hero.special_buff_dmg, '+')
                    hero.special_buff_flag = True
                else:
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
        time.sleep(2)
        clear_screen()

        cprint(f"You attacked {monster.name}!", ERROR, start_enter=1, wait_after=1)
        who_start = True
    else:
        clear_screen()
        battle_image()
        time.sleep(2)
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
            # print(f"{hero.defense}")
            # time.sleep(2)
            who_start = False
        # else:
        #     monster.attack(hero, monster.strength)
        #     who_start = True

        if monster.is_alive():
            if hero.special_buff_flag:
                hero.special_buff_iter += 1
                if hero.special_buff_iter > 3:
                    hero.special_buff(hero.special_buff_dmg, '-')
                    hero.special_buff_flag = False
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
            # hero.special_buff(hero.special_buff_dmg, '-')
            # hero.special_buff_iter = 0
            # hero.special_buff_flag = False
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

    # hero.add_items(monster.loot) TODO: to implement
    # return play_music("db/sounds/main_menu_start.mp3", infinite=True)
    # Item.add_to_inventory(hero, monster)
    pass
