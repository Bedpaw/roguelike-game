class STYLES:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    disable = '\033[02m'
    UNDERLINE = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'


class COLOR:
    WHITE = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    PURPLE = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    YELLOW = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'


class BG_COLOR:
    black = '\033[40m'
    RED = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


ERROR = COLOR.WHITE, BG_COLOR.RED, STYLES.BOLD
