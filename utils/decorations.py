from macros.COLORS import *


def cprint(string, *args):
    print(ctext(string, *args))
    pass


def ctext(string, *args):
    """
    :param string:[string] string to add styles
    :param args:[string with ansi]:[tuple strings with ansi] ALWAYS USE MACROS.COLORS WHERE ANSI IS DECODED
    :return: return colored string
    """
    reset = '\u001b[0m'
    styles = ''
    for style in args:
        if type(style) == tuple:
            for tuple_style in style:
                styles += tuple_style
        else:
            styles += style
    return f'{styles}{string}{reset}'

# EXAMPLES

# cprint("XD", COLOR.GREEN)
# cprint("XD", COLOR.WHITE, BG_COLOR.RED, STYLES.BOLD)
# cprint("XD", ERROR)  # Error is tuple with styles

# hero back
