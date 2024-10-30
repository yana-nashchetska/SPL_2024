# src/main.py
from src.input_handler import get_user_input
from src.font_selector import choose_font
from src.color_selector import choose_color
from src.ascii_art_creator import generate_ascii_art
from src.output_formatter import center_text
from src.preview import preview_art
from src.file_saver import save_to_file

def main():
    text = get_user_input()
    font = choose_font()
    color = choose_color()
    ascii_art = generate_ascii_art(text, font)
    ascii_art = center_text(ascii_art)
    colored_art = color + ascii_art + "\033[0m"  # \033[0m для скидання кольору

    if preview_art(colored_art):
        save_to_file(ascii_art)
