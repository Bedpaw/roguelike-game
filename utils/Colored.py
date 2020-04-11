class Colored:
    def __init__(self, string):
        self.string = string

    text_colors = {
        "white": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "gray": "\u001b[37m",
        "reset": "\u001b[0m",
    }
    bg_colors = {
        "black": "\u001b[40m",
        "red": "\u001b[41m",
        "green": "\u001b[42m",
        "yellow": "\u001b[43m",
        "blue": "\u001b[44m",
        "magenta": "\u001b[45m",
        "cyan": "\u001b[46m",
        "white": "\u001b[47m",
        "reset": "\u001b[0m",

    }
    decorators = {
        "B": "\u001b[1m",  # BOLD
        "U": "\u001b[4m",  # UNDERLINE
        "R": "\u001b[7m",  # REVERSE
        "reset": "\u001b[0m"
    }

    def cprint(self, color="reset", bg_color="reset", attrs="reset"):
        # text
        colored = u"" + self.text_colors[color] + self.string + self.bg_colors["reset"]

        # bg
        if bg_color != "reset":
            colored = u"" + self.bg_colors[bg_color] + colored + self.bg_colors["reset"]

        # attr
        if attrs != "reset":
            colored = u"" + self.decorators[attrs] + colored + self.decorators["reset"]

        print(colored)

    def available_colors_names(self):
        """
        Prints all available colors to use with example
        :return:pass
        """
        for key in self.bg_colors.keys():
            key = str(key)
            Colored(key).cprint(key)


