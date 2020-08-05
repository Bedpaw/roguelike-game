from utils.validation import int_input
from utils.utils import clear_screen


def pause_game_menu(game):
    board = game.current_board()
    hero = game.hero
    clear_screen()
    player_choice = None
    while player_choice is not 2:
        player_choice = int_input(
                '[1] Show active quest\'s\n'
                '[2] Back to game\n'
                '> '
                , 2
            )
        if player_choice == 1:
            show_quests(hero.quests)
        if player_choice == 2:
            board.print_board()



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
    if quests:
        for i, quest in enumerate(quests):
            if quest['COMPLETED']:
                status = "COMPLETED"
            else:
                status = "NOT COMPLETED"
            print(f"{i + 1}. NAME - {quest['name']}\n"
                  f"DESCRIPTION - {quest['description']}\n"
                  f"STATUS - {status}\n")
    else:
        print("You haven't take any quests")
    input("Press any key to back...")
