# Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на
# таблицу Brand)). Реализовать CRUD(создание, чтение, обновление по id,
# удаление по id) для бренда и машины. Создать пользовательский интерфейс.


def brand_choosing_param():
    print('\nChoose the parameter which you want to update:',
          '    1. Brand name',
          sep='\n')
    param_dict = {
        1: 'brand_name',
    }
    param_num = int(input('Your choice: '))
    return param_dict[param_num]


def car_choosing_param():
    print('\nChoose the parameter which you want to update:',
          '    1. Model',
          '    2. Release year',
          '    3. Brand',
          sep='\n')
    param_dict = {
        1: 'model',
        2: 'release_year',
        3: 'brand',
    }
    param_num = int(input('Your choice: '))
    return param_dict[param_num]
