def apply_color(ascii_art, color_mode):
    if color_mode == "bw":
        return ascii_art  # Нічого не змінюємо
    elif color_mode == "gray":
        gray_scale = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
        colored_art = []
        for line in ascii_art:
            colored_line = "".join(gray_scale[ord(char) % len(gray_scale)] for char in line)
            colored_art.append(colored_line)
        return colored_art
    return ascii_art
