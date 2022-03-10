cook_book = {}
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        food = line.strip()
        cook_book[food] = []
        counter = int(file.readline())
        list_of_ingridient = []
        for fac in range(counter):
            val, val1, val2 = file.readline().strip().split('|')
            ingredients = {'ingredient_name': val,
                           'quantity': int(val1),
                           'measure': val2}
            list_of_ingridient.append(ingredients)
            cook_book[food] += [ingredients]
        file.readline()


# print(cook_book)
# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }

def get_shop_list_by_dishes(dishes, person):
    all_dish_dict = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in all_dish_dict.keys():
                # prod_name = all_dish_dict[ingridient['ingredient_name']]['quantity']
                # print(prod_name)
                all_dish_dict[ingridient['ingredient_name']] = {
                    'quantity': ingridient['quantity'] * person + all_dish_dict[ingridient['ingredient_name']]['quantity'],'measure': ingridient['measure']}
            else:
                all_dish_dict[ingridient['ingredient_name']] = {'quantity': ingridient['quantity'] * person, 'measure': ingridient['measure']}


            #     all_dish_dict[ingridient['ingredient_name']] = {
            #         'quantity': ingridient['quantity'] + all_dish_dict[ingridient['ingredient_name']][
            #             'quantity'] * person}

    print(all_dish_dict)


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
