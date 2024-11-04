import os
import sys
from UI.user_interface import UserInterface

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(lab5_root)


def main():
    ui = UserInterface()
    ui.start()
