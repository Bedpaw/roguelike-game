def cprint(string, *args):
    reset = '\u001b[0m'
    styles = ''
    for style in args:
        if type(style) == tuple:
            for tuple_style in style:
                styles += tuple_style
        else:
            styles += style
    print(f'{styles}{string}{reset}')