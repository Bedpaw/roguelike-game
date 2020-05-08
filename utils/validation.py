from macros.COLORS import *


def check_int(s):
    if s != "":
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
    return False


def int_input(text_input, number_of_options=0, options=None, ):
    if options is None:
        options = []
    valid = False
    while not valid:
        s = input(text_input)
        if check_int(s):
            s = int(s)
            if options or number_of_options:
                if s in options or 0 < s <= number_of_options:
                    valid = True
                else:
                    cprint("INPUT OUT OF RANGE", ERROR)
            else:
                valid = True
        else:
            cprint("INPUT IS NOT INT", ERROR)
    return s
