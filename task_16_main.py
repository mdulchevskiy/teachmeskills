# pip instal sqlalchemy


# Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на
# таблицу Brand)). Реализовать CRUD(создание, чтение, обновление по id,
# удаление по id) для бренда и машины. Создать пользовательский интерфейс.


from task_16_funcs import *


def main():
    create_table()
    while True:
        print('\nChoose what you want to do:',
              '    1. Add a brand',
              '    2. Update the brand',
              '    3. Delete the brand',
              '    4. Print all brands',
              '    5. Add a car',
              '    6. Update the car',
              '    7. Delete the car',
              '    8. Print all cars',
              sep='\n')
        action_num = int(input('Your choice: '))
        if not action_num:
            break
        action_dict = {
            1: add_brand,
            2: brand_update,
            3: brand_delete,
            4: print_brands,
            5: add_car,
            6: car_update,
            7: car_delete,
            8: print_cars,
        }
        func = action_dict[action_num]
        func()


if __name__ == '__main__':
    main()
