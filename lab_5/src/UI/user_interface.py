from BLL.art_manager import ArtManager

class UserInterface:
    def start(self):
        print("Welcome to the ASCII Art 3D Generator!")
        
        shape = input("Enter the shape you want to create (cube/sphere): ").strip().lower()

        default_size = 5
        size_input = input(
            "Enter the size of the shape (default is {}): ".format(default_size)
        ).strip()

        size = int(size_input) if size_input.isdigit() else default_size

        symbol = input("Enter the symbol to use (default is '#'): ") or "#"

        art_manager = ArtManager()

        shape_instance = art_manager.create_shape(shape, size, symbol)
        art = art_manager.generate_art(shape_instance, symbol)

        print("\nGenerated ASCII Art:\n")
        print(art)
