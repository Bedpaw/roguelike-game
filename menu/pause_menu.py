from utils.validation import int_input
from utils.utils import clear_screen

def pause_game_menu(game):
    board = game.current_board()
    hero = game.hero
    clear_screen()
    while True:
        player_choice = int_input(
                '[1] Show active quest\'s\n'
                '[2] Show active quest\'s\n'
                '[3] Back to game\n'
                '> '
                , 3
            )
        if player_choice == 1:
            show_quests(hero.quests)
        if player_choice == 3:
            break


def show_quests(quests):
    """
    
    :param quests: 
    :return: 
    """"""
    Example quest
       'name': "TROLL KING",
       'description': "King Andrei has been wounded in fight with Troll King,"
                      "kill this monster to show King that you are brave enough to go east!",
       'COMPLETED': False,
       'reward': {
           'quest': "King's brave patent",
           'sword': 'Trolls slayer',  # TODO add item
           'gold': 1000
                           }
    """""
    for quest in quests:
        print(f"NAME - {quest['name']}\n"
              f"DESCRIPTION - {quest['description']}\n"
              f"STATUS - {quest['COMPLETED']}")
        input("Press any key to back...")