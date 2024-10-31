# src/main.py

from src.ascii_art_generator import generate_ascii_art

def main():
    user_text = input("Введіть текст для ASCII-арту: ")
    symbol_set = input("Введіть набір символів (наприклад, @, #, *): ")
    width = input("Введіть ширину ASCII-арту (натисніть Enter для значення за замовчуванням 40): ")
    height = input("Введіть висоту ASCII-арту (натисніть Enter для значення за замовчуванням 10): ")
    alignment = input("Оберіть вирівнювання (left, center, right): ")
    color_mode = input("Оберіть режим кольору (bw або gray): ")

    ascii_art = generate_ascii_art(
        user_text, 
        symbol_set or "*", 
        int(width or 40), 
        int(height or 10), 
        alignment or "center", 
        color_mode or "bw"
    )
    
    print(ascii_art)
