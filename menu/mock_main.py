from menu.log_in import log_in
from menu.main_menu import run_main_menu
from menu.main_menu import welcome_image


def main():


    print("WELCOME IN <GAME_NAME>\n")
    player_name = log_in()
    run_main_menu(player_name)


if __name__ == '__main__':
    main()