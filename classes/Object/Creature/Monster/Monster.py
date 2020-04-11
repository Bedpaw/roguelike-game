from classes.Object.Creature.Creature import Creature
import time
from utils.Colored import Colored


class Monster(Creature):
    type_of = "Monster"

    color_in_battle = "red"
    on_fight_message = "You have no chance with me! "  # print, when fight start
    on_die_message = "Argghr.."  # print, when hp < 0

    def on_defeat(self):
        Colored(self.name + " has been defeated!").cprint(color="white", bg_color="red", attrs="B")
        time.sleep(0.5)
        Colored(self.colon_name() + self.on_die_message).cprint(color=self.color_in_battle)

    def start_fight_message(self):
        Colored(self.colon_name() + self.on_fight_message).cprint(color=self.color_in_battle)

    exp = 30  # experience points for Hero, who kill monster
    loot = {
        "coins": 10
    }

