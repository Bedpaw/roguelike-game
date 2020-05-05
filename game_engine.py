def game_engine(game):
    while not game.endgame:
        game.board_changed = False
        my_board = game.current_board()
        while not game.board_changed and not game.endgame:
            my_board.print_board()
            my_board.get_user_choice()
            my_board.move_monsters()
            game.turn_counter += 1
            game.save_game(autosave=True)
