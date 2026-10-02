import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(BASE_DIR, "tasks")      # путь к файлу с заданиями
TESTS_FILE = os.path.join(BASE_DIR, "test.py")   # путь к файлу с тестами

TASKS = [
    ("0",  "Расстояния между городами", "distance0.py"),
    ("1",  "Круг и точка",              "circle1.py"),
    ("2",  "Операции (получить 25)",    "operations2.py"),
    ("3",  "Любимые фильмы",            "favorite_movies3.py"),
    ("4",  "Моя семья",                 "my_family4.py"),
    ("5",  "Зоопарк",                   "zoo5.py"),
    ("6",  "Песни",                     "songs_list6.py"),
    ("7",  "Секретное сообщение",       "secret7.py"),
    ("8",  "Сад и луг",                 "garden8.py"),
    ("9",  "Магазины",                  "shopping9.py"),
    ("10", "Склад",                     "store10.py"),
]


def print_menu():
    print("\nВыберите задание:")
    for num, title, _ in TASKS:
        print(f"  {num:>2}. {title}")
    print("   a. Запустить все задания")
    print("   t. Запустить тесты (pytest)")
    print("   q. Выход")


def run_file(filename):
    path = os.path.join(TASKS_DIR, filename)
    subprocess.run([sys.executable, path])


def run_one(num):
    for task_num, title, filename in TASKS:
        if task_num == num:
            print(f"\nЗадание {task_num}. {title}")
            run_file(filename)
            return
    print(f"Задание с номером '{num}' не найдено.")


def run_all():
    for num, title, filename in TASKS:
        print(f"\n Задание {num}. {title}")
        run_file(filename)


def run_tests():
    """Запускает pytest и передаёт ему путь к test.py."""
    print("\nЗапуск тестов")
    subprocess.run([
        sys.executable, "-m", "pytest",
        TESTS_FILE,
        "-v",
        "--no-header",
    ])

def main():
    print(" Лабораторная работа №1")

    while True:
        print_menu()
        choice = input("\nВаш выбор: ").strip().lower()

        if choice == "q":
            print("Выход.")
            break
        if choice == "a":
            run_all()
            continue
        if choice == "t":
            run_tests()
            continue
        run_one(choice)


if __name__ == "__main__":
    main()