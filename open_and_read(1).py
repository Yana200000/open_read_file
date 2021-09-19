from pprint import pprint
from collections import Counter

file = open("recipes3.txt", "w+")
file.write("""Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт""")

file.close()

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name) as my_file:
        for line in my_file:
            dish_name = line.strip()
            records_quantity = int(my_file.readline())
            ingredients_list = []
            for ingredients in range(records_quantity):
                ingredient_name, quantity, measure = my_file.readline().split('|')
                ingredients_list.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.replace('\n', '')}
                )
            result[dish_name] = ingredients_list
            my_file.readline()
        return result


cook_book = prepare_dict("recipes3.txt")
#pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    recipes = {}
    counter = Counter(dishes)
    for dish1 in counter.keys():
        for i in range(0, len(cook_book[dish1])):
            recipes['quantity'] = cook_book[dish1][i]['quantity'] * person_count * counter[dish1]
            recipes['measure'] = cook_book[dish1][i]['measure']
            recipes = {cook_book[dish1][i]['ingredient_name']: {'measure': recipes['measure'], 'quantity': recipes['quantity']}}
            print(recipes)


print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
print(get_shop_list_by_dishes(['Омлет'], 2))

