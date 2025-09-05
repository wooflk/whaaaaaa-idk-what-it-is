import subprocess
import sys

def install(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package])

def uninstall(package):
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package])

def upgrade(package):
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package])

def main():
    while True:
        print("1 - установить пакет")
        print("2 - удалить пакет")
        print("3 - обновить пакет")
        print("4 - выход")
        choice = input("выберите действие: ")

        if choice == "1":
            pkg = input("введите название пакета: ")
            install(pkg)
        elif choice == "2":
            pkg = input("введите название пакета: ")
            uninstall(pkg)
        elif choice == "3":
            pkg = input("введите название пакета: ")
            upgrade(pkg)
        elif choice == "4":
            print("выход")
            break
        else:
            print("неверный выбор")

if __name__ == "__main__":
    main()
