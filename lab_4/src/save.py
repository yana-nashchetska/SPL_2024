# src/save.py

def save_art_to_file(art):
    file_name = input("Введіть назву файлу для збереження (з .txt на кінці): ")
    with open(file_name, 'w') as file:
        file.write(art)
    print(f"ASCII-арт збережено у файл {file_name}.")
