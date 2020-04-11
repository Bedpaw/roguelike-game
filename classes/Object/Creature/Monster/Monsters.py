from classes.Object.Creature.Monster.Monster import Monster


class Troll(Monster):
    strength = 20
    hp = 200

    exp = 100
    loot = {
        "coins": 150,
        "troll_machete": 1
    }


class Arnold(Monster):
    strength = 20
    agility = 50
    luck = 100

    on_die_message = "I will be back"


