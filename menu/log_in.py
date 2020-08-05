def log_in():
    with open("db/saves/players.txt", "r+") as file:
        reader = file.readlines()[1:]
        player_name = input("Please enter your name before you start game.\nYour name:").upper()

        for row in reader:

            db_name, db_password = row.strip().split(",")

            while player_name == db_name:
                password = input(f"Hello again {player_name}! :)\nPlease enter your password: ")
                if password == db_password:
                    print("Entered password is correct!\n")
                    return player_name
                else:
                    print("Entered password is not correct!\n")

        with open("db/saves/players.txt", "a+") as f:
            password_new = input(f"Hello {player_name}!\nPlease set your new password: ")
            f.write("\n" + player_name + "," + password_new)

            return player_name
