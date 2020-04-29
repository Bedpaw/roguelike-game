from classes.Object.Object import MyObject
from utils.decorations import cprint
from utils.key_service import key_pressed
from macros import OBJECT_TYPES
from macros.COLORS import *
from random import *
# from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monster import Monster
from utils.validation import int_input
# from events.Battle import

# hero = Hero(name="Franek")
# monster = Monster(name="Goblin")


class Item:
    """Abstract class without place on map, eg. loots from monsters"""

    def __init__(self,
                 item_type="sword",
                 name="set_name",
                 hp=0,
                 max_hp=0,
                 strength=0,
                 agility=0,
                 luck=0):

        self.item_type = item_type
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.agility = agility
        self.luck = luck

    def add_power(self, hero):
        hero.strength += self.strength
        hero.hp += self.hp
        hero.max_hp += self.max_hp
        hero.agility += self.agility
        hero.luck += self.luck

    def del_power(self, hero):
        hero.strength -= self.strength
        hero.hp -= self.hp
        hero.max_hp -= self.max_hp
        hero.agility -= self.agility
        hero.luck -= self.luck


    @classmethod
    def gloves(cls, agility=5):
        names = ["Magic gloves", "Gloves of Goblins"]
        return cls(agility=agility, item_type="gloves", name=choice(names))
    @classmethod
    def helmet(cls, item_type, name, strength):
        return cls(item_type, name, strength)

    @classmethod
    def sword(cls, item_type, name, strength):
        return cls(item_type, name, strength)

    @classmethod
    def armor(cls, item_type, name, strength):
        return cls(item_type, name, strength)

    @classmethod
    def belt(cls, item_type, name, strength):
        return cls(item_type, name, strength)

    @classmethod
    def shield(cls, item_type, name, agility):
        return cls(item_type, name, agility)

    @classmethod
    def trousers(cls, item_type, name, agility):
        return cls(item_type, name, agility)

    @classmethod
    def boots(cls, item_type, name, agility): #strength, agility, stamina, energy
        return cls(item_type, name, agility)

    @classmethod
    def wand(cls, item_type, name, agility):
        return cls(item_type, name, agility)

    @classmethod
    def healing_potion(cls, item_type, name, stamina):
        return cls(item_type, name, stamina)

    @classmethod
    def mana(cls, item_type, name, energy):
        return cls(item_type, name, energy)

    @classmethod
    def key(cls, item_type, name):
        return cls(item_type, name)



# treasure = [Item.gloves("gloves", "Magic gloves", 5),
#             Item.gloves("gloves", "Gloves of pain", 8),
#             Item.helmet("helmet", "Odin's horns", 8),
#             Item.helmet("helmet", "Warriors' helmet", 7),
#             Item.sword("sword", "Sword for stinky Trolls", 7),
#             Item.sword("sword", "Ultralight dagger", 6),
#             Item.armor("armor", "Dragon's scales", 15),
#             Item.armor("armor", "Titanium armor", 14),
#             Item.wand("wand", "Wand of Hobbits", 5),
#             Item.wand("wand", "Harry Potter wand", 7),
#             Item.belt("belt", "Snake skin belt", 2),
#             Item.belt("belt", "Karate black belt", 3),
#             Item.trousers("trousers", "King Arthur's pantaloons", 6),
#             Item.trousers("trousers", "Leather trousers", 5),
#             Item.boots("boots", "Boots of luck", 3),
#             Item.boots("boots", "Clover boots", 8),
#             Item.healing_potion("hpotion", "Papa Smurf's healing potion", 50),
#             Item.healing_potion("hpotion", "EXTRA COOL potion", 100),
#             Item.healing_potion("hpotion", "Porter beer + cocaine", 120),
#             Item.healing_potion("hpotion", "Honey and milk", 40),
#             Item.mana("mpotion", "Power is back potion", 10),
#             Item.mana("mpotion", "Gummibear potion", 12),
#             Item.key("key", "steel key"),
#             Item.key("key", "copper key")
#             ]


class Treasure(MyObject):
    """Class with treasures, treasure is chooseng item from items"""

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
            cprint("You have found a chest and you've opened it", INFO)
            print(f'You took from chest {self.loot[0].name}')
            hero.inventory[self.loot[0].item_type] = self.loot[0]
            return True

    def which_item_in_chest(self, treasure):  # losuje item z dostępnych w grze
        loot = []
        loot.append(choice(treasure))
        return loot


chest = Treasure("chest", is_locked=True)  # tworze obiekt z wybranym parametrem
# chest.open_treasure(hero) #wywoluje funkcje z obiektu z parametrem hero
# print(Item().add_to_inventory(monster.loot, hero))