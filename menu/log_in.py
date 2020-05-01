def log_in():

    with open("db/saves/players.txt", "r+") as file:
        reader = file.readlines()[1:]
        player_name = input("NAME").upper()

        for row in reader:

            db_name, db_password = row.strip().split(",")

            while player_name == db_name:
                password = input("PASSWORD:")
                if password == db_password:
                    print("Pass correct")
                    return player_name
                else:
                    print("Pass not correct")

        with open("db/saves/players.txt", "a+") as f:
            password_new = input("PASSWORDNEW:")
            f.write("\n" + player_name + "," + password_new)

            return player_name