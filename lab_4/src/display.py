def display_ascii_art(ascii_art):
    print("\nВаш ASCII-арт:\n")
    for line in ascii_art:
        print(line)

def preview_ascii_art(ascii_art):
    print("\nПопередній перегляд:\n")
    for line in ascii_art[:5]:  # Перегляд лише перших 5 рядків
        print(line)
    print("\n...")
