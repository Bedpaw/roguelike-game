from menu.log_in import log_in
from menu.main_menu import run_main_menu
from menu.main_menu import welcome_image
from utils.decorations import cprint

def welcome_image():
    with open ("default.txt", "r") as f:
        for row in f:
            cprint((row[:-1]), BG_COLOR.WHITE, COLOR.DARKGREY, STYLES.BOLD)



def main():


    print("WELCOME IN <GAME_NAME>\n")
    welcome_image()
    player_name = log_in()
    run_main_menu(player_name)




if __name__ == '__main__':
    main()