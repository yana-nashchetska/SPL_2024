def get_user_input():
    user_text = input("Введіть текст для ASCII-арту: ")
    symbol_set = input("Введіть набір символів (наприклад, @, #, *): ")
    width = int(input("Введіть ширину ASCII-арту (натисніть Enter для значення за замовчуванням 40): ") or 40)
    height = int(input("Введіть висоту ASCII-арту (натисніть Enter для значення за замовчуванням 10): ") or 10)
    alignment = input("Оберіть вирівнювання (left, center, right): ").lower()
    color_mode = input("Оберіть режим кольору (bw або gray): ").lower()
    return user_text, symbol_set, width, height, alignment, color_mode
