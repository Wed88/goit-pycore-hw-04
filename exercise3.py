import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory(path):
    root = Path(path)

    if not root.exists():
        print(Fore.RED + f"Помилка: Шлях '{path}' не існує.")
        return
    if not root.is_dir():
        print(Fore.RED + f"Помилка: Шлях '{path}' не є директорією.")
        return

    print(Fore.GREEN + f"Структура директорії: {root}")

    def print_structure(directory, indent=""):
        for item in sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name)):
            if item.is_dir():
                print(indent + Fore.BLUE + f"📂 {item.name}")
                print_structure(item, indent + "  ")
            else:
                print(indent + Fore.YELLOW + f"📜 {item.name}")

    print_structure(root)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python exercise3.py /шлях/до/директорії")
    else:
        visualize_directory(sys.argv[1])
