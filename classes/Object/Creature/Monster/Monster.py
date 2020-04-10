from ..Creature import Creature
import time


class Monster(Creature):
    type_of = "Monster"

    on_fight_message = "You have no chance with me! "  # print, when fight start
    on_die_message = "Argghr.."  # print, when hp < 0

    def on_defeat(self):
        print(self.name + " has been defeated!")
        time.sleep(0.5)
        print(self.name + ": " + self.on_die_message)
    exp = 30  # experience points for Hero, who kill monster
    loot = {
        "coins": 10
    }
