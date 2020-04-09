from ..Creature import Creature


class Monster(Creature):
    type_of = "Monster"

    on_fight_message = "You have no chance with me! "  # print, when fight start
    on_die_message = "Argghr.."  # print, when hp < 0

    exp = 30  # experience points for Hero, who kill monster
    loot = {
        "coins": 10
    }
