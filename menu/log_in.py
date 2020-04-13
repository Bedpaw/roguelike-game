def log_in():
    password_correct = False
    player_name = None
    while not password_correct:
        player_name = input("Please provide your name: ").upper()

        # Search in saves/players.csv if player name exist:
        is_in_database = True    # MOCK

        # If player is in database store his password here:
        password = "XXX"    # MOCK

        if is_in_database:
            # existing player
            user_password = input("Hello again!\n"
                                  "Please provide your password\n"
                                  "Password: ")

            if user_password == password:
                password_correct = True
                # saves/$player_name$ already exist
            else:
                print("Your password is incorrect")
        else:
            # new player
            user_password = input("Hello!\n"
                                  "Please provide your password\n"
                                  "Password: ")
            # write players name and password to saves/players.csv
            # create folder with player name in saves
            password_correct = True

    return player_name
