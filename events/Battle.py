import time
from utils.validation import int_input
from macros import BATTLE_MODES
from macros.COLORS import *
from utils import key_service
from utils.utils import clear_screen


def battle(hero, monster, battle_mode, hero_start=True):
    """
    :param hero_start:[bool] True if hero start fight, False if monster, npc
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
        if battle_mode == BATTLE_MODES.MANUAL_FIGHT:
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

    def block_skill_counter():
        pass

    def use_potions():
        key_pressed = key_service.key_pressed()
        if key_pressed.lower() == 'h':
            hero.use_hpotion()

        elif key_pressed.lower() == 'm':
            hero.use_mana()

    def how_many_potions(kind_of_potion):
        counter = 0
        for potion in hero.backpack:
            if potion.item_type == kind_of_potion:
                counter += 1
        return counter

    def print_skill_selection():
        spell_name_print = ''
        max_key = 2
        for k, v in hero.spells.items():
            if k is 9:
                spell_name_print += f"{' ' * 8}[{k}]{' ' * 2}Hero HP:{hero.hp}{' ' * 4}| {' ' * 2}Hero Mana: {hero.mana}\n"
                spell_name_print += f"{' ' * 11}{'-' * 40}\n"
                spell_name_print += f"{' ' * 20}HP Potions |  MANA Potions \n"
                spell_name_print += f"{' ' * 4}[key:quantity]  H:{how_many_potions('healing_potion')}{' ' * 11}" \
                                    f"M: {how_many_potions('mana')}"

            else:
                if hero.energy >= v[4]:
                    if v[2] == 'energy_and_stamina':
                        spell_name_print += f"{' ' * 8}[{k}] {v[0]} (mana cost:{v[1]})\n"
                    else:
                        skill = calculate_dmg(v[2], v[3])
                        spell_name_print += f"{' ' * 8}[{k}] {v[0]} [dmg:{int(skill)}] (mana cost:{v[1]})\n"
                    max_key += 1
        spell_name_print += '\nYour choice how to fight: '
        return max_key, spell_name_print

    def hero_move():

        if battle_mode == BATTLE_MODES.MANUAL_FIGHT:
            valid = True
            while valid:
                max_key, spell_name_print = print_skill_selection()

                max_key_options = [item for item in range(1, max_key - 1)]

                max_key_options += [9]

                hero_attack = int_input(spell_name_print, options=max_key_options)
                if hero_attack == 9:
                    print("Press [h] to use hp potion or [m] to use mana potion")
                    time.sleep(0.5)
                    use_potions()

                    continue
                else:
                    spell_mana_cost = hero.spells[hero_attack][1]
                    wait(0.5)

                    if spell_mana_cost >= hero.mana:
                        print(f"You dont have enough mana ({hero.mana}) to use this spell.")
                        time.sleep(0.5)
                        valid = True
                    else:
                        hero.mana -= spell_mana_cost
                        valid = False

                if hero.spells[hero_attack][2] == 'energy_and_stamina':

                    if 0 < hero.special_buff_iter <= 6:
                        print('You have already this buff on')
                        time.sleep(1)
                        continue
                    else:
                        hero.special_buff_flag = True
                        hero.special_buff(hero.special_buff_dmg, '+')
                else:
                    calc_dmg = calculate_dmg(hero.spells[hero_attack][2], hero.spells[hero_attack][3])
                    hero.attack(monster, calc_dmg)


    # Battle start messages
    if hero_start:
        clear_screen()
        battle_image()
        time.sleep(1)
        clear_screen()
        cprint(f"You attacked {monster.name}!", ERROR, start_enter=1, wait_after=1)

    else:
        clear_screen()
        battle_image()
        time.sleep(1)
        clear_screen()
        cprint(f'{hero.name} has been attacked by {monster.name}!', ERROR, start_enter=1, wait_after=1)

    cprint(f"Battle start! {hero.name} vs {monster.name}", COLOR.PURPLE, start_enter=1, end_enter=1)
    hero.start_fight_message()
    monster.start_fight_message()

    # Battle
    whose_turn = False
    round_counter = 0
    while monster.is_alive():
        round_counter += 1
        cprint(f"Round: {round_counter}", COLOR.PURPLE)

        if hero.special_buff_flag:
            if hero.special_buff_iter >= 0 and hero.special_buff_iter <= 3:
                hero.special_buff_iter += 1
                print(f"{BG_COLOR.RED}{STYLES.BOLD}{COLOR.WHITE}hero defense + {hero.special_buff_dmg}{STYLES.RESET}\n")
            else:
                hero.special_buff(hero.special_buff_dmg, '-')
                print(f"{BG_COLOR.RED}{STYLES.BOLD}{COLOR.WHITE}hero defense - {hero.special_buff_dmg}{STYLES.RESET}\n")
                hero.special_buff_iter = 0
                hero.special_buff_flag = False

        if whose_turn is False:
            cprint(f'{hero.name} attacks!', hero.color_in_battle)
            hero_move()
            cprint(f"Monster's hp: {monster.hp}/{monster.max_hp}", COLOR.RED)
            whose_turn = True
            wait(1)
            print("\n")


        if monster.is_alive() and whose_turn == True:
            monster.attack(hero, monster.strength)
            hero.print_hp()
            hero.print_mana()
            whose_turn = False
            wait(1)

        else:
            if hero.special_buff_flag:
                hero.special_buff_iter = 0
                hero.special_buff(hero.special_buff_dmg, '-')
                hero.special_buff_flag = False
            monster.print_hp()
            monster.on_defeat()
            wait(1)
            break


        if not hero.is_alive():
            hero.print_hp()
            input("You die!")
            return True

    # Battle end
    cprint(f'You have got {monster.exp} exp.', SUCCESS)
    hero.get_exp(monster.exp)

    hero.add_to_backpack(monster.loot)
    hero.print_loot(monster.loot)

    input("\nPress enter to exit fight report...\n")
    hero.add_to_message_box(f"Glorious victory! {monster.name} has been vanquished!")

    if monster.name == "Belzedup":
        hero.game.endgame = True
    pass
