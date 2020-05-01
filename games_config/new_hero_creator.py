from classes.Object.Creature.Hero.Hero import Hero



# Difficulty level as param if need
import time
from macros import COLORS
from utils.key_service import *
from classes.Object.Creature.Hero.Hero_Breed.Knight import Knight
from classes.Object.Creature.Hero.Hero_Breed.Sorcerer import Sorcerer
from classes.Object.Creature.Hero.Hero_Breed.Palladin import Palladin

select_type = {
    "0": [COLORS.COLOR.RED, "Knight", COLORS.STYLES.RESET, Knight],
    "1": [COLORS.COLOR.BLUE, "Sorcerer", COLORS.STYLES.RESET, Sorcerer],
    "2": [COLORS.COLOR.GREEN, "Palladin", COLORS.STYLES.RESET, Palladin]
}

def create_new_hero():
    valid_key = False  # change to True if key is valid AND move is possible
    current_key = 4
    while not valid_key:
        clear_screen()
        print('Select class you want to play [w/s] and press enter:')
        for k, v in select_type.items():
            if k == str(current_key):
                print(f"%s{COLORS.BG_COLOR.LIGHTGREY}[{k}]. {v[1]}{v[2]}" % (' ' * 8))
            else:
                print(f"%s{v[0] + v[0]}[{k}]. {v[1]}{v[2]}" % (' ' * 8))
        key = key_pressed()

        if ord(key) == 115:
            current_key += 1
        elif ord(key) == 119:
            current_key -= 1
        elif ord(key) == 13:
            return select_type[str(current_key)][3]('Wojtek')
        else:
            print("not [w] or [s] pressed")
            time.sleep(0.5)

        if current_key >= 3:
            if ord(key) == 115:
                current_key = 0
            elif ord(key) == 119:
                current_key = 2
        else:
            if current_key == 3 and ord(key) == 115:
                current_key = 0
            if current_key < 0:
                current_key = 3 - abs(current_key)
