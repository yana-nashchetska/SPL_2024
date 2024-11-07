import sys
import os

# Додаємо кореневу папку проекту
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Додаємо папку `src` до шляху
src_path = os.path.join(project_root, "lab_5", "src")
sys.path.insert(0, src_path)

# Імпортуємо main з src
from main import main

if __name__ == "__main__":
    main()
