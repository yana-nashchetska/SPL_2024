
import os
import sys


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from .UI.console.ConsoleUI import ConsoleUI


def main():
    ui = ConsoleUI()
    ui.display_menu()
