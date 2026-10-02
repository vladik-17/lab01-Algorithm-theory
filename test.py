import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(BASE_DIR, "tasks")


def run_task(filename):
    """Запускает файл задания и возвращает его stdout как строку."""
    path = os.path.join(TASKS_DIR, filename)
    result = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    # отладка: если что-то не так — увидим причину
    if result.returncode != 0:
        print("STDERR:", result.stderr)
        print("STDOUT:", result.stdout)
        print("RETURN CODE:", result.returncode)
        print("PATH:", path)
        print("EXISTS:", os.path.exists(path))
    return result.stdout


#  00. Расстояния 
def test_distance_runs():
    out = run_task("distance0.py")
    assert "Moscow" in out


#  01. Круг 
def test_circle_runs():
    out = run_task("circle1.py")
    lines = out.strip().splitlines()
    assert lines and lines[0].replace(".", "").isdigit()


#  02. Операции 
def test_operations_returns_25():
    out = run_task("operations2.py")
    assert "25" in out


#  03. Фильмы 
def test_movies_contains_titles():
    out = run_task("favorite_movies3.py")
    assert "Терминатор" in out


#  04. Семья 
def test_family():
    out = run_task("my_family4.py")
    assert "Рост отца" in out


#  05. Зоопарк 
def test_zoo():
    out = run_task("zoo5.py")
    assert "bear" in out


#  06. Песни 
def test_songs():
    out = run_task("songs_list6.py")
    assert "Три песни звучат" in out


#  07. Секрет 
def test_secret():
    out = run_task("secret7.py")
    assert "в бане веник дороже денег" in out


#  08. Сад 
def test_garden():
    out = run_task("garden8.py")
    assert "ромашка" in out


#  09. Магазины 
def test_shopping():
    out = run_task("shopping9.py")
    assert "пятерочка" in out


#  10. Склад 
def test_store():
    out = run_task("store10.py")
    assert "Лампа - 27 шт, стоимость 1134 руб" in out