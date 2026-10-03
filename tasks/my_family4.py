# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама', 'папа', 'брат', 'я']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['мама', 168],
    ['папа', 182],
    ['брат', 155],
    ['я', 180],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# TODO здесь ваш код
# Ищем отца и печатаем его рост
#for member in my_family_height:
   # if member[0] == 'папа':
        #print(f'Рост отца - {member[1]} см')

## Суммируем рост всех членов семьи
#total = sum(member[1] for member in my_family_height)
#print(f'Общий рост моей семьи - {total} см')

def get_father_height(family_height):
    for member in family_height:
        if member[0] == 'папа':
            return member[1]
    return None


def get_total_height(family_height):
    return sum(member[1] for member in family_height)


def run():
    print(f'Рост отца - {get_father_height(my_family_height)} см')
    print(f'Общий рост моей семьи - {get_total_height(my_family_height)} см')


if __name__ == "__main__":
    run()