from classes.Object.Creature.Monster.Monster import Monster
from events.Battle import battle
from macros.COLORS import *
from macros import OBJECT_TYPES
from macros import MOVES_TYPES
from utils.decorations import cprint
from utils.validation import int_input
from macros import DIFFICULTY_LEVEL
from utils.utils import clear_screen
from classes.Object.Item.Item import Item


class NPC(Monster):
    conversation_folder_path = 'db/conversations/'
    color_in_battle = COLOR.RED
    in_conversation_color = COLOR.PURPLE
    field_move_possible = True

    def __init__(self, name="Set_me_name", symbol_on_map="M", position_x=-1, position_y=-1,
                 strength=100,
                 hp=200,
                 max_hp=200,
                 agility=10,
                 luck=0,
                 move_type=MOVES_TYPES.STAY,
                 move_param=None,
                 conversation_file_name='example1.txt',
                 loot=None,
                 exp=300,
                 dialog_index=0,
                 on_die_message="Stop, you won, you can pass...",
                 on_fight_message="I warned you...",
                 color_on_board=COLOR.PURPLE,
                 field_color=BG_COLOR.BLUE,
                 quest_func=None
                 ):
        super().__init__(name, symbol_on_map, position_x, position_y,
                         strength, hp, max_hp, agility, luck, move_type, move_param,
                         loot, exp, on_fight_message, on_die_message)

        if quest_func is None:
            quest_func = []
        self.dialog_index = dialog_index
        self.start_dialog = self.conversation_folder_path + conversation_file_name
        self.dialogs_path = [self.start_dialog]
        self.color_on_board = color_on_board
        self.field_color = field_color
        if quest_func is None:
            self.quest_func = []
        else:
            self.quest_func = quest_func

    def on_meet(self, hero):
        """
        Function to out if hero meet NPC
        :param hero:
        :return:pass
        """
        clear_screen()
        conversation_effects = self.__conversation(self.dialog_path(hero), hero)
        return self.__do_after_conversation(conversation_effects, hero)

    def dialog_path(self, hero):
        """
        Basic version: read and return as a list lines from txt files:
        This function should be overwritten in child class if you want to change dialog path despite of some conditions
        :return:[list] indentation_store
        """
        dialog_path = self.dialogs_path[self.dialog_index]
        return self.read_dialog_from_file(dialog_path)

    def __do_after_conversation(self, func, hero):
        """
        Run function despite of conversation result
        :param func:STRING: returned from txt.file string interpretation of functions
        :param hero: that take part in conversation with NPC
        :return:False if hero can't move after conversation else True
        """
        if func == "BATTLE":
            battle(hero, self, hero.game.battle_mode)
            return True
        if func == "TRADE":
            self.trade(hero)
        if func == "END":
            clear_screen()
        if func.startswith("QUEST"):
            quest_index = func.split('T')[1]
            self.quest_func[int(quest_index)](hero)
        return False

    def trade(self, hero):
        cprint(f'{self.name} that\'s my best items', COLOR.WHITE, BG_COLOR.GREEN)

        # To implement

    def __conversation(self, indentation_store, hero):
        """
        :param indentation_store:
        :param hero:
        :return:
        """

        def color_option(option):
            """
            Change line color in conversation
            :param option:
            :return:
            """
            color = COLOR.WHITE
            if "BATTLE" in option:
                color = COLOR.RED
            elif "END" in option:
                color = COLOR.LIGHTGREY
            elif "TRADE" in option:
                color = COLOR.GREEN
            elif "QUEST" in option:
                color = COLOR.YELLOW
            return color

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
                    color = color_option(option)
                    if j in next_header_options or i == 1:
                        cprint(option, color)
            # HEADERS
            elif i % 2 == 0:
                # print("ENDS", ends_index)
                # print("OPTIONS", next_header_options)
                number_of_options = len(next_header_options)  # input validation
                user_choice = int_input(f'{hero.color_on_board}{STYLES.BOLD}{hero.name}: {STYLES.RESET}',
                                        number_of_options)
                if i == 2:
                    # check if user pick function ending conversation
                    if user_choice - 1 in ends_index:
                        #   print(functions_to_output[ends_index.index(user_choice - 1)])
                        return functions_to_output[ends_index.index(user_choice - 1)]

                    move_index = 1
                    for index in ends_index:
                        if index < user_choice:
                            move_index += 1

                    # Take from text information about header to output and his options index
                    next_header_text, options_index = indentation[user_choice - move_index].split("&")
                    next_header_options = []
                    for index in options_index:
                        next_header_options.append(int(index))
                    # Print header
                    cprint(f'\n{self.name}: {next_header_text}\n', self.in_conversation_color, STYLES.BOLD)

                else:
                    # check if user pick function ending conversation
                    if next_header_options[user_choice - 1] in ends_index:
                        #   print(functions_to_output[ends_index.index(next_header_options[user_choice - 1])])
                        return functions_to_output[ends_index.index(next_header_options[user_choice - 1])]

                    move_index = 0
                    for index in ends_index:
                        if index < next_header_options[user_choice - 1]:
                            move_index += 1

                    # Take from text information about header to output and his options index
                    next_header_text, options_index = indentation[
                        next_header_options[user_choice - 1] - move_index].split("&")
                    next_header_options = []
                    for index in options_index:
                        next_header_options.append(int(index))
                    # Print header
                    cprint(f'\n{self.name}: {next_header_text}\n', self.in_conversation_color, STYLES.BOLD)

    @staticmethod
    def read_dialog_from_file(text_file):
        """

        :param text_file:
        indentation = "  "
        headers text
        option always start with [1], [2], [3] etc..
        &... in headers (except line 1) you have to write which options of next indentation are connected with this header
        &... for options that end dialog -> this string will be returned from dialog function

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


        :return:lines from text_file:list of lists: [
                                [string, string, string...]
                                [all lines with 0 indentation]
                                [all lines with 1 indentation]
                                etc...
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

    # <---------------------------------- NPC ---------------------------------->
    @classmethod
    def gimme_beer_guard(cls):
        pass

    @classmethod
    def eastern_guard(cls, pos_x, pos_y):
        eastern_guard = cls(
            name="Eastern_guard",
            position_x=pos_x,
            position_y=pos_y,
            symbol_on_map='G',
            field_color=BG_COLOR.LIGHTGREY)

        def on_meet(hero):
            if hero.quest_done_by_name("TROLL KING"):
                return True
            else:
                print("STOP, you can't move east!")

        eastern_guard.on_meet = on_meet
        return eastern_guard
