import time
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monsters import Monster, Troll, Arnold
from utils.Colored import Colored

hero = Hero("Andrzej", "X", 1, 1)
Troll = Troll("Troll", "T", 1, 2)
Arnold1 = Arnold("Arni", "O", 1, 1)
Arnold2 = Arnold("Arni", "O", 1, 1)

IMMEDIATE_FIGHT = 0
AUTOMATE_FIGHT = 1
MANUAL_FIGHT = 2


def battle(hero, monster, battle_mode="AUTOMATE_FIGHT"):
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
        if battle_mode == "AUTOMATE_FIGHT":
            time.sleep(wait_time)

    def hero_move():
        if battle_mode == "MANUAL_FIGHT":
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
    Colored("\nBattle start! " + hero.name + " vs " + monster.name + '\n').cprint("magenta")
    hero.start_fight_message()
    monster.start_fight_message()
    print("")

    # Battle
    round_counter = 0
    while monster.is_alive():
        wait(1)
        round_counter += 1
        Colored("Round: " + str(round_counter)).cprint("magenta")
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


# test [IMMEDIATE_FIGHT, AUTOMATE_FIGHT, MANUAL_FIGHT]
battle(hero, Arnold1, "IMMEDIATE_FIGHT")
# battle(hero, Troll)
# battle(hero, Arnold2)
# print(hero.strength, hero.exp)
