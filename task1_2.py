with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingridient_count = int(file.readline().strip())
        ingridient = []
        for i in range(ingridient_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            ingridient.append({'ingredient_name': ingredient_name,
                               'quantity': quantity,
                               'measure': measure
                               })
        file.readline()
        cook_book[dish] = ingridient
    print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        list_by_dishes = {}
        for dish in dishes:
            if dish in cook_book:
                for ingridient in cook_book[dish]:
                    new_list=dict(ingridient)
                    new_list['quantity']=str(int(new_list['quantity'])*person_count)
                    if new_list['ingredient_name'] not in list_by_dishes:
                        list_by_dishes[new_list['ingredient_name']]=new_list
                    else:
                        list_by_dishes[new_list['ingredient_name']]['quantity']+=new_list
        return list_by_dishes
    new = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(new)