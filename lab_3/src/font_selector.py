import pyfiglet

def choose_font():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Доступні шрифти:", ", ".join(fonts[:10]), "...")  # Вивід перших 10 шрифтів
    font = input("Оберіть шрифт для ASCII-арту: ")
    return font if font in fonts else "standard"  # Повернути стандартний шрифт, якщо введено невірний
