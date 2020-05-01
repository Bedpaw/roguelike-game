import csv

def log_in():
    password_correct = False
    player_name = None
    while not password_correct:
        player_name = input("Please provide your name: ").upper()

        with open("../db/saves/players.csv", "r+", newline="") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if player_name.upper() == row[0]:
                   user_password = input("Hello again!\n"
                                  "Please provide your password\n"
                                  "Password: ")
                    if user_password == row[1]:
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

log_in()