def load_recipes(f_name):
    cook_book = {}
    with open(f_name , encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for i in range(ingredient_count):
                parts = f.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': parts[0],
                    'quantity': int(parts[1]),
                    'measure': parts[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book

print(load_recipes('recipes.txt'))

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient_ in cook_book[dish]:
            name = ingredient_['ingredient_name']
            measure = ingredient_['measure']
            quantity = ingredient_['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book=load_recipes('recipes.txt')))

files = ['1.txt', '2.txt', '3.txt']
data = []

def merge_files(files, result_file):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            data.append((file, len(lines), lines))
    data.sort(key=lambda x: x[1])
    with open(result_file, 'w', encoding='utf-8') as res:
        for file_name, count, lines in data:
            res.write(f'{file_name}\n')
            res.write(f'{count}\n')
            res.writelines(lines)
            res.write('\n')
            return 'Check a new-created file'

print(merge_files(['1.txt', '2.txt', '3.txt'], 'result.txt'))