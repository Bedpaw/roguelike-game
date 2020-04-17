from classes.Object.Creature.Creature import Creature
from macros import MOVES_TYPES, BATTLE_MODES
from macros.COLORS import *
from utils.decorations import cprint
from classes.Object.Creature.Hero.Hero import Hero
from classes.Object.Creature.Monster.Monsters import Arnold
from events.Battle import battle
from utils.validation import int_input


class NPC(Creature):
    move_type = MOVES_TYPES.STAY
    in_conversation_color = COLOR.PURPLE

    __dialog_index = 0
    __dialogs_path = ['test.txt', 'test3.txt']
    on_die_message = "Stop, you won, you can pass..."
    on_fight_message = "I warned you..."

    def on_meet(self, hero):
        dialog_path = self.__dialogs_path[self.__dialog_index]
        dialogs = read_dialog_from_file(dialog_path)
        conversation_effects = self.__conversation(dialogs, hero)
        self.__do_after_conversation(conversation_effects, hero)

    def __do_after_conversation(self, func, hero):
        if func == "BATTLE":
            battle(hero, self)
        if func == "TRADE":
            self.__trade(hero)

    def __color_option(self, option):
        color = COLOR.WHITE
        if "BATTLE" in option:
            color = COLOR.RED
        elif "END" in option:
            color = COLOR.LIGHTGREY
        elif "TRADE" in option:
            color = COLOR.GREEN
        return color

    def __trade(self, hero):
        cprint(f'{self.name} that\'s my best items', COLOR.WHITE, BG_COLOR.GREEN)
        # To implement

    def __conversation(self, indentation_store, hero):

        ends_index = []
        next_header_options = []
        functions_to_output = []

        for i, indentation in enumerate(indentation_store):
            if i == 0:
                cprint(f'{self.name}: {indentation[i]}\n', self.in_conversation_color)
                next_header_options = indentation_store[1]  # only for validation first input
            # OPTIONS
            elif i % 2 == 1:
                ends_index = []
                functions_to_output = []
                for j, option in enumerate(indentation):
                    if "&" in option:
                        ends_index.append(j)
                        functions_to_output.append(option.split('&')[1])
                    color = self.__color_option(option)
                    if j in next_header_options or i == 1:
                        cprint(option, color)
            # HEADERS
            elif i % 2 == 0:
                number_of_options = len(next_header_options)  # input validation
                user_choice = int_input(f'{hero.color_on_board}{STYLES.BOLD}{hero.name}: ', number_of_options)

                # check if user pick function ending conversation
                if user_choice - 1 in ends_index:
                    return functions_to_output[ends_index.index(user_choice - 1)]

                move_index = 1
                for index in ends_index:
                    if index < user_choice:
                        move_index += 1
                next_header_options = []

                # Take from text information about header to output and his options index
                next_header_text, options_index = indentation[user_choice - move_index].split("&")
                for index in options_index:
                    next_header_options.append(int(index))

                # Print header
                cprint(f'\n{self.name}: {next_header_text}\n', self.in_conversation_color, STYLES.BOLD)


def read_dialog_from_file(text_file):
    """

    :param text_file:
    indentation = "  "
    headers text
    option always start with [1], [2], [3] etc..
    &... in headers (except line 1) you have to write which options of next indentation are connected with this header
    &... for options that end dialog

    EXAMPLE:
    Stop don't move or I will kill you!
      [1] Slow down, let's talk...
        I don't have time for talking, what do you want? &012  <-- U HAVE TO WRITE ALL OPTIONS HERE
          [1] Why are you so angry?                             <- 0
            I have to stay here all day long, when all my friends drinking beer in pub. &0          <--- 0
              [1] Hmm... maybe I have some idea... &END
          [2] Me neither! Get out from my way! &BATTLE          <- 1
          [3] OK, I won't waste your time! &END                 <- 2
      [2] Get out from my way! &BATTLE
      [3] Ok, ok, chill out
        Something other &3                                      <    !!!!!
          [1] option &END                                       <- 3 !!!!!


    :return:list of lists: [
    [all lines with 0 indentation]
    [all lines with 1 indentation
                            ]
    """
    def longest_indentation_in_line():
        counter = 0
        for char in line:
            if char == " ":
                counter += 1
            else:
                return counter

    with open(text_file, 'r') as f:
        lines = f.readlines()

        # Find biggest indentation
        biggest_indentation = 0
        for line in lines:
            max_in = longest_indentation_in_line()
            if max_in > biggest_indentation:
                biggest_indentation = max_in

        # Create store list for dialog lines in all indentations
        indentation_store = [[] for i in range(int(biggest_indentation / 2) + 2)]

        # Sort dialogs to proper indentations
        for line in lines:
            indentation_index = int(longest_indentation_in_line() / 2)
            line = line.lstrip()[:-1]  # Remove indentations and \n
            indentation_store[indentation_index].append(line)
        return indentation_store


path = 'test.txt'
guard = NPC("Guard", "A", 1, 1)
monster = Arnold("Guard", "A", 2, 2)
hero = Hero("Andrzej", "A", 3, 4)

guard.on_meet(hero)
