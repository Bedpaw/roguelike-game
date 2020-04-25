from classes.Object.Object import MyObject
from utils.decorations import cprint
from macros import OBJECT_TYPES
from macros.COLORS import *
from random import *
from classes.Object.Creature.Hero.Hero import Hero
from utils.validation import int_input

hero = Hero(name="Franek")

class Item:

    def __init__(self, item_type="sword", name="set_name", hp=0, max_hp=0, strength=0, agility=0, luck=0):
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
    def gloves(cls) -> object:
        return cls(item_type="gloves", name="Magic gloves", agility=5)

    @classmethod
    def helmet(cls):
        return cls(item_type="helmet", name="Golden helmet", strength=10)

    @classmethod
    def sword(cls):
        return cls(item_type="sword", name="Sword of Goblins", strength=20)

    @classmethod
    def armor(cls):
        return cls(item_type="armor", name="King Gordon's armor", strength=25)

    @classmethod
    def belt(cls):
        return cls(item_type="belf", name="Candy pinky belt", strength=5)

    @classmethod
    def shield(cls):
        return cls(item_type="shield", name="", agility=5)

    @classmethod
    def healing_potion(cls):
        return cls(item_type="healing_potion", name="Gummibear potion", max_hp=100)

    @classmethod
    def mana(cls):
        cls(item_type="mana", name="Papa smurf mana", luck=10)

    @classmethod
    def key(cls):
        return cls(item_type="key", name="")

    @classmethod
    def coins(cls):
        cls(item_type="coins", name="Golden coins")

    def add_to_inventory(self,hero):
        pass #TODO


treasure = [Item.gloves(), #TODO stworzyć róźne warianty tych itemów
            Item.helmet(),
            Item.sword(),
            Item.armor(),
            Item.belt(),
            Item.healing_potion(),
            Item.mana(),
            Item.key(),
            Item.coins()
            ]


class Treasure(MyObject):

    def __init__(self, name="Set_me_name", symbol_on_map="$", position_x=-1, position_y=-1, is_locked=False,
                 message_in_field=""):

        super().__init__(name, symbol_on_map, position_x, position_y)
        self.message_in_field = message_in_field
        self.is_locked = is_locked

    def open_treasure(self, hero):
        """
        opening chest, choosing item in it
        this return is giving info to board is field is empty or not
        """

        if self.is_locked:
            cprint("You have found closed chest, do you want to look into? ", INFO)
            answer = int_input("[1] Yes\n[2] No\n", 2)
            if answer == 1:
                if hero.is_in_inventory("key"):
                    loot = self.which_item_in_chest(treasure)
                    if loot[0].item_type in hero.inventory:
                        if "coins" in hero.inventory:
                            hero.inventory["coins"] += 100
                        else:
                            hero.inventory["coins"] = 100
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


    def which_item_in_chest(self, treasure): # losuje item z dostępnych w grze
        loot = []
        loot.append(choice(treasure))
        return loot


    def if_in_inventory(self):
        pass #TODO

    def add_to_inventory(self):
        pass #TODO


chest = Treasure("chest", is_locked=True) #tworze obiekt z wybranym parametrem
chest.open_treasure(hero) #wywoluje funkcje z obiektu z parametrem hero
