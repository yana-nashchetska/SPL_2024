# runner.py

import sys
import os

base_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(base_dir, "src"))
sys.path.append(os.path.join(base_dir, "shared"))

from src.main import main
lab5_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, lab5_root)

if __name__ == "__main__":
    main()

