from random import *
# from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monster import Monster
from classes.Object.Object import MyObject
from macros.COLORS import *
from utils.validation import int_input

# hero = Hero(name="Franek")
monster = Monster(name="Goblin")


class Item:
    """Abstract class without place on map, eg. loots from monsters"""

    def __init__(self,
                 item_type="sword",
                 name="set_name",
                 hp=0,
                 max_hp=0,
                 strength=0,
                 agility=0,
                 stamina=0,
                 energy=0):
        self.item_type = item_type
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.agility = agility
        self.energy = energy
        self.stamina = stamina

    def add_power(self, hero):
        hero.strength += self.strength
        hero.hp += self.hp
        hero.max_hp += self.max_hp
        hero.agility += self.agility
        hero.energy += self.energy
        hero.stamina += self.stamina

    def del_power(self, hero):
        hero.strength -= self.strength
        hero.hp -= self.hp
        hero.max_hp -= self.max_hp
        hero.agility -= self.agility
        hero.energy -= self.energy
        hero.stamina -= self.stamina

    @classmethod
    def gloves(cls, agility=5):
        names = ["Magic gloves", "Gloves of Goblins"]
        return cls(agility=agility, item_type="gloves", name=choice(names))

    @classmethod
    def helmet(cls, strength=8):
        names = ["Odin's horns", "Warriors' helmet"]
        return cls(strength=strength, item_type="helmet", name=choice(names))

    @classmethod
    def sword(cls, strength=15):
        names = ["Sword of pain", "Cutting edge", "Assasin's Dagger", "King's Arthur sword"]
        return cls(strength=strength, item_type="sword", name=choice(names))

    @classmethod
    def armor(cls, strength=25):
        names = ["Dragon's armor", "Burning armor of hell", "Devil's skin", "Grizzlie bear's fur"]
        return cls(strength=strength, item_type="armor", name=choice(names))

    @classmethod
    def belt(cls, strength=10):
        names = ["Snake skin belt", "Poor cloth belt"]
        return cls(strength=strength, item_type="belt", name=choice(names))

    @classmethod
    def shield(cls, agility=15):
        names = ["Captain America shield", "Stainless steel shield"]
        return cls(agility=agility, item_type="gloves", name=choice(names))

    @classmethod
    def trousers(cls, agility=5):
        names = ["Alligator skin pants", "Leather pants"]
        return cls(agility=agility, item_type="gloves", name=choice(names))

    @classmethod
    def boots(cls, agility=8):  # strength, agility, stamina, energy
        names = ["Light leather boots", "Steel boots"]
        return cls(agility=agility, item_type="gloves", name=choice(names))

    @classmethod
    def wand(cls, energy=20):
        names = ["Wooden wand", "Wand of Fire"]
        return cls(energy=energy, item_type="gloves", name=choice(names))

    @classmethod
    def healing_potion(cls, stamina=150):
        names = ["Papa Smurf's healing potion", "EXTRA COOL potion", "Porter beer + cocaine", "Honey and milk"]
        return cls(stamina=stamina, item_type="healing_potion", name=choice(names))

    @classmethod
    def mana(cls, energy=150):
        names = ["Power is back potion", "Gummibear potion"]
        return cls(energy=energy, item_type="mana", name=choice(names))

    @classmethod
    def key(cls):
        return cls(cls, item_type="key", name="Golden key")

    @classmethod
    def quest_item(cls, name):
        return cls(item_type="quest", name=name)


treasure = [
    Item.gloves,
    Item.helmet,
    Item.sword,
    Item.armor,
    Item.wand,
    Item.belt,
    Item.trousers,
    Item.boots,
    Item.healing_potion,
    Item.mana,
    Item.key
]


class Treasure(MyObject):
    """Class with treasures, treasure is choosing item from items"""

    def __init__(self,
                 name="Set_me_name",
                 symbol_on_map="$",
                 position_x=-1, position_y=-1,
                 is_locked=False,
                 message_in_field=""):

        super().__init__(name, symbol_on_map, position_x, position_y)
        self.message_in_field = message_in_field
        self.is_locked = is_locked

    def open_treasure(self, hero):
        """
        opening chest, choosing item in it
        this return is giving info to board is field is empty or not
        if hero has already this item, he gets 100 coins instead
        """

        if self.is_locked:

            cprint("You have found closed chest, do you want to look into? ", INFO)
            answer = int_input("[1] Yes\n[2] No\n", 2)
            if answer == 1:
                if hero.is_in_inventory("key"):
                    loot = self.which_item_in_chest(treasure)
                    if loot[0].item_type in hero.inventory:
                        if "coins" in loot:
                            hero.coins += 100
                            print(f'You have gain 100 coins!')
                    else:
                        print(f'You took from chest {loot[0].name}')
                        hero.inventory[loot[0].item_type] = loot[0]
                    return True
                else:
                    print(f"You don't have key in your inventory")
                    return False
            else:
                cprint("You left closed chest on it\'s place")
                return False
        else:
            loot = self.which_item_in_chest(treasure)
            cprint("You have found a chest and you've opened it", INFO)
            print(f'You took from chest {loot[0].name}')
            hero.inventory[loot[0].item_type] = loot[0]
            return True

    def which_item_in_chest(self, treasure):  # losuje item z dostępnych w grze
        loot = []
        loot.append(choice(treasure)())
        return loot


# print(which_item_in_chest(self,treasure))
#
# chest = Treasure("chest", is_locked=True)  # tworze obiekt z wybranym parametrem
# chest.open_treasure(hero) #wywoluje funkcje z obiektu z parametrem hero
# print(Item().add_to_inventory(monster.loot, hero))
