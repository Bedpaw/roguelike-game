import os
from macros.COLORS import *


def print_image(path):
    with open(path, "r") as f:
        for row in f:
            cprint((row[:-1]), BG_COLOR.WHITE, COLOR.LIGHTGREEN, STYLES.BOLD)


def clear_screen():
    if os.name == "nt":
        os.system('cls')
        print_image("menu/welcome_image.txt")
    else:
        os.system('clear')
        print_image("menu/welcome_image.txt")


def hard_clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
