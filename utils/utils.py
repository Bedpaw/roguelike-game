import os
from macros.COLORS import *


def welcome_image():
    with open("menu/default.txt", "r") as f:
        for row in f:
            cprint((row[:-1]), BG_COLOR.WHITE, COLOR.LIGHTGREEN, STYLES.BOLD)


def clear_screen():
    if os.name == "nt":
        os.system('cls')
        welcome_image()
    else:
        os.system('clear')
        welcome_image()


def hard_clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
