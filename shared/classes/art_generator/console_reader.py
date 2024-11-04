class ConsoleReader:
    def read_text():
        return input("Введіть текст для ASCII-арту: ")

    def read_symbol_set():
        return input("Введіть набір символів (наприклад, @, #, *): ")

    def read_width():
        width = input("Введіть ширину ASCII-арту (натисніть Enter для значення за замовчуванням 40): ")
        return int(width) if width.isdigit() else 40

    def read_height():
        height = input("Введіть висоту ASCII-арту (натисніть Enter для значення за замовчуванням 10): ")
        return int(height) if height.isdigit() else 10

    def read_alignment():
        return input("Оберіть вирівнювання (left, center, right): ")

    def read_color_mode():
        return input("Оберіть режим кольору (bw або gray): ")
