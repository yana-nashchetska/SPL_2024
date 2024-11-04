def get_user_text():
    """Get the text for ASCII art from the user."""
    return input("Введіть текст для ASCII-арту: ")

def get_user_font():
    """Display available fonts and get the user's font choice."""
    fonts = ['slant', 'block', 'bubble', 'digital']
    print("Доступні шрифти:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")
    try:
        choice = int(input("Оберіть номер шрифту: ")) - 1
        return fonts[choice] if 0 <= choice < len(fonts) else 'slant'
    except ValueError:
        print("Невірний вибір. Вибрано шрифт за замовчуванням 'slant'.")
        return 'slant'

def get_user_color():
    """Display available colors and get the user's color choice."""
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    print("Доступні кольори:")
    for color in colors:
        print(color)
    color = input("Введіть колір: ").lower()
    return color if color in colors else 'white'  # Повертає 'white' за замовчуванням, якщо колір недійсний

def get_user_symbol():
    """Get the symbol to use for ASCII art, or return None for the default."""
    symbol = input("Введіть символ для ASCII-арту (або залиште пустим для стандартного): ")
    return symbol if symbol else None

def get_user_confirmation(prompt):
    """Get a yes/no confirmation from the user."""
    return input(prompt).strip().lower() == 'так'

def get_user_width():
    """Get the desired width for ASCII art from the user, or return default 80 if not specified."""
    width = input("Введіть бажану ширину ASCII-арту (або залиште пустим для стандартної ширини): ")
    return int(width) if width.isdigit() else 80  # Повертає 80 за замовчуванням
