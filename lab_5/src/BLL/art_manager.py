import os
import sys

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if lab5_root not in sys.path:
    sys.path.insert(0, lab5_root)

main_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(main_root)

from shared.classes.art_generator.ascii_art_generator import ArtGenerator
from shared.classes.art_generator.shapes import Cube, Sphere
from shared.classes.art_generator.shapes import ArtGenerator


class ArtManager:
    def create_shape(self, shape_type, size, symbol):
        if shape_type == "cube":
            return Cube(size, symbol)
        elif shape_type == "sphere":
            return Sphere(size, symbol)
        else:
            raise ValueError("Unknown shape type")

    def generate_art(self, shape_instance, symbol):
        art_generator = ArtGenerator(shape_instance, symbol)
        return art_generator.generate()
