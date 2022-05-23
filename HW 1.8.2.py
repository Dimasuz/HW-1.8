from pprint import pprint

with open('recipest.txt', encoding='utf-8') as file_cook:
    cook_book = {}

    for line in file_cook:

        dish = line.strip()
        cook_book[dish] = []
        num = int(file_cook.readline())

        for item in file_cook:
            if item == '\n':
                break
            ing = item.strip().split(' | ')
            ingredient = {}
            ingredient['ingredient_name'] = ing[0]
            ingredient['quantity'] = ing[1]
            ingredient['measure'] = ing[2]
            cook_book[dish].append(ingredient)


# pprint(cook_book)

# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for i in cook_book[dish]:
            if i['ingredient_name'] in result.keys():
                result[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
            else:
                dic_temp = {}
                dic_temp['measure'] = i['measure']
                dic_temp['quantity'] = int(i['quantity']) * person_count
                result[i['ingredient_name']] = dic_temp

    pprint(result)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
