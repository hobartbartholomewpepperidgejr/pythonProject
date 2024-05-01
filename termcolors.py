def tcolor(color):

    colors = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "pink": 35,
        "cyan": 36,
        "white": 37
    }
    return("\u001b["+str(colors[color])+"m")