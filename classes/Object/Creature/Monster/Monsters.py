from classes.Object.Creature.Monster.Monster import Monster


class Troll(Monster):
    strength = 20
    hp = 200

    exp = 100
    loot = {
        "coins": 150,
        "troll_machete": 1
    }


# Example fight
spider = Monster("Spider1", "s", 1, 1)
spider2 = Monster("Spider2", "s", 1, 1)
spider3 = Monster("Spider3", "s", 1, 1)
spider4 = Monster("Spider4", "s", 1, 1)
troll = Troll("Troll", "t", 2, 2)


def fight():
    counter = 0
    spiders_wins = False
    troll_win = False
    while not troll_win and not spiders_wins:
        counter += 1
        print("Round: " + str(counter))
        if spider.is_alive():
            spider.attack(troll)
        if spider2.is_alive():
            spider2.attack(troll)
        if spider3.is_alive():
            spider3.attack(troll)
        if spider4.is_alive():
            spider4.attack(troll)
        if spider.is_alive():
            troll.attack(spider)
        elif spider2.is_alive():
            troll.attack(spider2)
        elif spider3.is_alive():
            troll.attack(spider3)
        elif spider4.is_alive():
            troll.attack(spider4)
        if not (spider.is_alive() or spider2.is_alive() or spider3.is_alive() or spider4.is_alive()):
            print("Troll win!")
            troll_win = True
        elif not troll.is_alive():
            print("Spiders wins!")
            spiders_wins = True


fight()
