def align_text(text, width, alignment):
    if alignment == "left":
        return text.ljust(width)
    elif alignment == "center":
        return text.center(width)
    elif alignment == "right":
        return text.rjust(width)
    return text
