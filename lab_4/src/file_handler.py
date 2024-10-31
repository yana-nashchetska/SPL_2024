def save_to_file(ascii_art):
    save_option = input("Зберегти ASCII-арт у файл? (y/n): ").lower()
    if save_option == "y":
        filename = input("Введіть ім'я файлу для збереження: ")
        with open(filename, "w") as file:
            for line in ascii_art:
                file.write(line + "\n")
        print(f"ASCII-арт збережено у файл {filename}")
