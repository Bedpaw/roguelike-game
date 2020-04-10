import time
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monsters import Monster, Troll, Arnold

# test
hero = Hero("Andrzej", "X", 1, 1)
Troll = Troll("Troll", "T", 1, 2)
Arnold1 = Arnold("Arni", "O", 1, 1)
Arnold2 = Arnold("Arni", "O", 1, 1)


def battle(hero, monster):
    # Prefix for fight:
    hero_do = hero.name + ": "
    monster_do = monster.name + ": "

    # Battle start messages
    print("Battle start! " + hero.name + " vs " + monster.name + '\n')
    print(hero_do + hero.on_fight_message)
    print(monster_do + monster.on_fight_message + '\n')
    # time.sleep(1)

    # Battle
    round_counter = 0
    while monster.is_alive():
        round_counter += 1
        print("Round: " + str(round_counter))
        # time.sleep(0.5)

        hero.attack(monster)

        if monster.is_alive():
            monster.print_hp()
            # time.sleep(1)
            monster.attack(hero)
            hero.print_hp()
            # time.sleep(1)
        else:
            monster.print_hp()
            # time.sleep(1)
            monster.on_defeat()

        if not hero.is_alive():
            hero.print_hp()
            print("FUNCTION ENDING GAME")
            break

    # Battle end
    hero.get_exp(monster.exp)
    # hero.add_items(monster.loot) TODO: to implement

    pass

# test
# battle(hero, Arnold1)
# battle(hero, Troll)
# battle(hero, Arnold2)
# print(hero.strength, hero.exp)