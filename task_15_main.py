# pip install sqlalchemy


# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.


from task_15_funcs import (add_product,
                   product_delete,
                   product_update,
                   print_table,
                   create_table)


def main():
    create_table()
    while True:
        print('\nChoose what you want to do:',
              '    1. Add a product',
              '    2. Update the product',
              '    3. Delete the product',
              '    4. Read the database',
              sep='\n')
        action_num = int(input('your choice: '))
        if not action_num:
            break
        action_dict = {
            1: add_product,
            2: product_update,
            3: product_delete,
            4: print_table, }
        func = action_dict[action_num]
        func()


if __name__ == '__main__':
    main()
