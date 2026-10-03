import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(BASE_DIR, "tasks")

# ВАЖНО: sys.path и импорт идут ПОСЛЕ объявления BASE_DIR
sys.path.insert(0, BASE_DIR)
from tasks import my_family4  # noqa: E402


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

def lines_of(out):
    return [line.strip() for line in out.strip().splitlines() if line.strip()]

#  00. Расстояния 
def test_distance_runs():
    out = run_task("distance0.py")
    expected = (
        "{'Moscow': {'London': 145.6, 'Paris': 130.38}, "
        "'London': {'Moscow': 145.6, 'Paris': 42.43}, "
        "'Paris': {'Moscow': 130.38, 'London': 42.43}}"
    )
    assert out.strip() == expected


#  01. Круг 
def test_circle_runs():
    out = run_task("circle1.py")
    assert lines_of(out) == ["5541.7693", "True", "False", "False"]
# 

#  02. Операции 
def test_operations_returns_25():
    out = run_task("operations2.py")
    assert lines_of(out) == ["9", "25"]


#  03. Фильмы 
def test_movies_contains_titles():
    out = run_task("favorite_movies3.py")
    assert lines_of(out) == [
        "Терминатор",
        "Назад в будущее",
        "Пятый элемент",
        "Чужие",
        "Чужие",
        "Пятый элемент",
        "Назад в будущее",
        "Терминатор",
    ]


#  04. Семья 
#def test_family():
    #out = run_task("my_family4.py")
    #assert lines_of(out) == [
        #"Рост отца - 182 см",
        #"Общий рост моей семьи - 685 см",
   # ]
# c семьей мы проверяем саму функцию суммирования роста

def test_family():
    # Проверяем саму функцию суммирования роста
    total = my_family4.get_total_height(my_family4.my_family_height)
    expected = sum(member[1] for member in my_family4.my_family_height)
    assert total == expected

    # Проверяем рост отца
    father = my_family4.get_father_height(my_family4.my_family_height)
    assert father == 182

    # Проверяем конкретное значение суммы
    assert total == 685


#  05. Зоопарк 
def test_zoo():
    out = run_task("zoo5.py")
    assert lines_of(out) == [
        "['lion', 'bear', 'kangaroo', 'elephant', 'monkey']",
        "['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']",
        "['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']",
        "Лев сидит в клетке номер 1",
        "Жаворонок сидит в клетке номер 7",
    ]


#  06. Песни 
def test_songs():
    out = run_task("songs_list6.py")
    assert lines_of(out) == [
        "Три песни звучат 14.93 минут",
        "А другие три песни звучат 13.49 минут",
    ]


#  07. Секрет 
def test_secret():
    out = run_task("secret7.py")
    assert lines_of(out) == ["в бане веник дороже денег"]



#  08. Сад 
def test_garden():
    out = run_task("garden8.py")
    lines = [line.strip() for line in out.strip().splitlines() if line.strip()]

    assert eval(lines[0]) == ["гладиолус", "клевер", "мак", "одуванчик", "подсолнух", "роза", "ромашка"]
    assert eval(lines[1]) == ["одуванчик", "ромашка"]
    assert eval(lines[2]) == ["гладиолус", "подсолнух", "роза"]
    assert eval(lines[3]) == ["клевер", "мак"]

#  09. Магазины 
def test_shopping():
    out = run_task("shopping9.py")
    assert lines_of(out) == [
        "печенье: [{'shop': 'ашан', 'price': 10.99}, {'shop': 'пятерочка', 'price': 9.99}, {'shop': 'магнит', 'price': 11.99}]",
        "конфеты: [{'shop': 'ашан', 'price': 34.99}, {'shop': 'пятерочка', 'price': 32.99}, {'shop': 'магнит', 'price': 30.99}]",
        "карамель: [{'shop': 'ашан', 'price': 45.99}, {'shop': 'пятерочка', 'price': 46.99}, {'shop': 'магнит', 'price': 41.99}]",
        "пирожное: [{'shop': 'ашан', 'price': 67.99}, {'shop': 'пятерочка', 'price': 59.99}, {'shop': 'магнит', 'price': 62.99}]",
    ]


#  10. Склад 
def test_store():
    out = run_task("store10.py")
    assert lines_of(out) == [
        "Лампа - 27 шт, стоимость 1134 руб",
        "Стол - 54 шт, стоимость 27860 руб",
        "Диван - 3 шт, стоимость 3550 руб",
        "Стул - 105 шт, стоимость 10311 руб",
    ]