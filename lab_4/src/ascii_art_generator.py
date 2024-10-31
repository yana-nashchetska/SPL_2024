# src/ascii_art_generator.py

from src.font_library import get_ascii_font
import textwrap

def generate_ascii_art(text, symbol="*", width=40, height=10, alignment="center", color_mode="bw"):
    if alignment not in ["left", "center", "right"]:
        print("Невідоме вирівнювання. Використовується вирівнювання за замовчуванням (center).")
        alignment = "center"

    font = get_ascii_font(symbol)
    base_height = 5
    max_chars_per_line = width // 6  # орієнтовна кількість літер на рядок

    # Розбивка тексту на рядки з урахуванням ширини
    wrapped_text = textwrap.wrap(text, max_chars_per_line)

    # Генерація ASCII-арту для кожного рядка
    ascii_art_lines = []
    for line in wrapped_text:
        lines = [""] * base_height
        for char in line.upper():
            if char in font:
                char_lines = font[char]
                for i in range(base_height):
                    lines[i] += char_lines[i] + " "
            else:
                for i in range(base_height):
                    lines[i] += " " * 6  # порожній простір для невідомого символу

        # Застосовуємо вирівнювання до кожного рядка окремо
        for i in range(len(lines)):
            if alignment == "center":
                lines[i] = lines[i].center(width)
            elif alignment == "right":
                lines[i] = lines[i].rjust(width)
            else:
                lines[i] = lines[i].ljust(width)

        ascii_art_lines.extend(lines)

    # Обрізаємо за висотою, якщо необхідно
    if height < len(ascii_art_lines):
        ascii_art_lines = ascii_art_lines[:height]

    # Додаємо кольоровий режим (сіру гаму) якщо обрано
    if color_mode == "gray":
        ascii_art_lines = [line.replace(symbol, '\033[90m' + symbol + '\033[0m') for line in ascii_art_lines]

    return "\n".join(ascii_art_lines)
