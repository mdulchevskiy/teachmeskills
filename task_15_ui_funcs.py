# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.


def choosing_param():
    print('\nChoose the parameter which you want to update:',
          '    1. Название',
          '    2. Цена',
          '    3. Количество',
          '    4. Комментарий',
          sep='\n')
    param_dict = {
        1: 'title',
        2: 'price',
        3: 'amount',
        4: 'comment', }
    param_num = int(input('your choice: '))
    return param_dict[param_num]


def choosing_id(table):
    print('\nAvailable ID:')
    for product in table:
        print(product.id, end=' ')
    print('\nChoose the ID:')
    chosen_id = input('your choice: ')
    return chosen_id
