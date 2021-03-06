import time


def cprint(string, *args, start_enter=0, end_enter=0, wait_after=0):
    print(start_enter * "\n" + ctext(string, *args) + '\n' * end_enter)
    time.sleep(wait_after)
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
