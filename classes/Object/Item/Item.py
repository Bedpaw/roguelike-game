from random import choice
from classes.Object.Object import MyObject

from utils.validation import int_input
from utils.utils import clear_screen
from macros.COLORS import *


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
                 mana=0,
                 energy=0):
        self.item_type = item_type
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.agility = agility
        self.energy = energy
        self.stamina = stamina
        self.mana = mana



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
        return cls(agility=agility, item_type="shield", name=choice(names))

    @classmethod
    def trousers(cls, agility=5):
        names = ["Alligator skin pants", "Leather pants"]
        return cls(agility=agility, item_type="trousers", name=choice(names))

    @classmethod
    def boots(cls, agility=8):  # strength, agility, stamina, energy
        names = ["Light leather boots", "Steel boots"]
        return cls(agility=agility, item_type="boots", name=choice(names))

    @classmethod
    def wand(cls, energy=20):
        names = ["Wooden wand", "Wand of Fire"]
        return cls(energy=energy, item_type="wand", name=choice(names))

    @classmethod
    def healing_potion(cls, hp=150):
        names = "Papa Smurf's healing potion", "EXTRA COOL potion", "Porter beer + cocaine", "Honey and milk"
        return cls(hp=hp, item_type="healing_potion", name=choice(names))

    @classmethod
    def mana(cls, mana=150):
        names = ["Power is back potion", "Gummibear potion"]
        return cls(mana=mana, item_type="mana", name=choice(names))

    @classmethod
    def key(cls):
        return cls(item_type="key", name="Golden key")

    @classmethod
    def quest_item(cls, name="Flamethrower for really hard monsters", strength=30):
        return cls(strength=strength, item_type="quest", name=name)

    @staticmethod
    def item_types():
        return {
            1: "gloves",
            2: "helmet",
            3: "armor",
            4: "shield",
            5: "belt",
            6: "boots",
            7: "trousers"
        }

treasure = [
    Item.gloves,
    Item.helmet,
    Item.sword,
    Item.armor,
    # Item.wand,
    Item.belt,
    Item.trousers,
    Item.boots,
    Item.healing_potion,
    Item.mana,
    Item.quest_item
    # Item.key
]


class Treasure(MyObject):
    """Class with treasures, treasure is choosing item from items"""

    def __init__(self,
                 name="Wooden chest",
                 symbol_on_map="$",
                 position_x=-1, position_y=-1,
                 is_locked=False,
                 message_in_field="Whooaa! What is this? A chest?"):

        super().__init__(name, symbol_on_map, position_x, position_y)
        self.message_in_field = message_in_field
        self.is_locked = is_locked
        self.color_on_board = COLOR.LIGHTCYAN
        self.field_move_possible = True

    def open_treasure(self, hero):
        """
        opening chest, choosing item in it
        this return is giving info to board is field is empty or not
        if hero has already this item, he gets 100 coins instead
        """
        print(self.message_in_field)
        if self.is_locked:
            clear_screen()
            cprint("You have found closed chest, do you want to look into? ", INFO)
            answer = int_input("[1] Yes\n[2] No\n", 2)
            if answer == 1:
                if hero.is_in_backpack("Golden key"):
                    loot = self.which_item_in_chest(treasure)
                    # if loot[0].item_type in hero.backpack:
                    if loot[0].item_type == "coins":
                        hero.coins += 100
                        hero.add_to_message_box(f'You have gain 100 coins!')
                    else:
                        hero.add_to_message_box(f'You took from chest {loot[0].name}')
                        hero.backpack.append(loot[0])
                    return True
                else:
                    hero.add_to_message_box(f"You don't have key in your inventory")
                    return False
            else:
                hero.add_to_message_box("You left closed chest on it\'s place")
                return False
        else:
            hero.add_to_message_box("You have found a chest and you've opened it")
            loot = self.which_item_in_chest(treasure)
            hero.add_to_message_box(f'You took from chest {loot[0].name}')
            hero.backpack.append(loot[0])
            return True


    def which_item_in_chest(self, treasure):
        """
        function is choosing from available treasures
        Returns: choosen lot in function
        """
        loot = []
        loot.append(choice(treasure)())
        return loot

