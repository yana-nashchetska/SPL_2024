import pyfiglet


def generate_ascii_art(text, font="standard"):
    return pyfiglet.figlet_format(text, font=font)
