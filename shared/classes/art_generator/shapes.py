import math
from shared.classes.art_generator.ascii_art_generator import ArtGenerator
from shared.libs.font_library import get_ascii_font


class Shape3D:
    def __init__(self, size=5):
        self.size = size

    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")


class Cube:
    def __init__(self, size, symbol):
        self.size = size
        self.symbol = symbol  # Store the symbol as an attribute

    def draw(self, symbol=None):  # Add parameter for symbol
        if symbol is None:
            symbol = self.symbol  # Use instance symbol if none provided
        width = self.size * 2
        height = self.size + 5
        return draw_cube(width, height, symbol)  # Use the provided or instance symbol


def draw_cube(width, height, symbol):  # Add parameter symbol
    cube = [[" "] * width for _ in range(height)]

    # Define vertices of the cube
    vertices = {
        "tc": (width // 2, 0),
        "tl": (0, int(0.25 * height)),
        "tr": (width - 1, int(0.25 * height)),
        "cc": (width // 2, int(0.5 * height)),
        "bl": (0, int(0.75 * height)),
        "br": (width - 1, int(0.75 * height)),
        "bc": (width // 2, height - 1),
    }

    # Define edges of the cube
    edges = (
        ("tc", "tl"),
        ("tc", "tr"),
        ("tl", "cc"),
        ("tr", "cc"),
        ("bl", "bc"),
        ("br", "bc"),
        ("cc", "bc"),
    )

    for edge in edges:
        v1 = vertices[edge[0]]
        v2 = vertices[edge[1]]
        x1, y1 = v1
        x2, y2 = v2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        try:
            m = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            for yy in range(min(y1, y2), max(y1, y2) + 1):
                cube[yy][x1] = symbol
        else:
            yy = y1
            for xx in range(x1, x2 + 1):
                cube[int(round(yy))][xx] = symbol
                yy += m

    cube_str = "\n".join("".join(row) for row in cube)
    return cube_str


class Sphere:
    def __init__(self, size, symbol):
        self.size = size
        self.symbol = symbol

    def draw(self, symbol):
        output = []
        for i in range(-self.size, self.size + 1):
            row = []
            for j in range(-self.size, self.size + 1):
                if math.sqrt(i**2 + j**2) <= self.size:
                    row.append(symbol)
                else:
                    row.append(" ")
            output.append("".join(row).rstrip())

        return "\n".join(output)


class Art3DGenerator(ArtGenerator):
    def __init__(
        self, shape: Shape3D, symbol="*", width=40, height=10, color_mode="bw"
    ):
        super().__init__(
            "", symbol, width, height, "center", color_mode
        )
        self.shape = shape

    def generate_3d_art(self):
        ascii_art = self.shape.draw(self.symbol)
        self.text = ascii_art
        return ascii_art
