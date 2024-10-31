from src.ascii_art_generator import ArtGenerator
from src.console_reader import ConsoleReader
from src.console_writer import ConsoleWriter

def main():
    # Зчитуємо дані від користувача
    text = ConsoleReader.read_text()
    symbol = ConsoleReader.read_symbol_set()
    width = ConsoleReader.read_width()
    height = ConsoleReader.read_height()
    alignment = ConsoleReader.read_alignment()
    color_mode = ConsoleReader.read_color_mode()

    # Створюємо генератор ASCII-арту
    art_generator = ArtGenerator(text, symbol, width, height, alignment, color_mode)
    ascii_art = art_generator.generate()

    # Виводимо результат
    ConsoleWriter.display_art(ascii_art)
