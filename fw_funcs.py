import json
import csv
from datetime import datetime


def engine_settings() -> str:
    """Выбор типа хранения данных.

    Возвращает в переменную engine способ хранения данных и делает ее глобальной для использования в
    остальных функциях.
    """
    global engine
    print('Before we start, choose the engine',
          '    1. JSON',
          '    2. CSV',
          sep='\n')
    while True:
        choice = input('Your choice (number): ')
        try:
            choice = int(choice)
        except ValueError:
            print('Incorrect input. Enter a number.')
        else:
            if choice == 1:
                engine = 'json'
                break
            elif choice == 2:
                engine = 'csv'
                break
            else:
                print('Incorrect input. Enter only 1 or 2.')
    return engine


def create_database() -> dict:
    """Создание базы данных.

    Создание БД происходит через определение пользователя по умолчанию в виде словаря.
    """
    header = ['ID', 'First name', 'Last name', 'Birth date', 'Profession']
    default_user = ['111111', 'Maxim', 'Dulchevskiy', '29.01.1997', 'junior developer']
    database = {'1 user': dict(zip(header, default_user))}
    return database


def write_database(database: dict, engine: str):
    """Запись базы данных в файл.

    В зависимости от ранее выбранного способа хранения данных (engine) и типа переменной database, происходит запись
    БД в файл в необходимом формате.
    """
    if engine == 'json':
        if isinstance(database, list):
            database = from_csv_to_json(database)
        with open('database.txt', 'w') as datafile:
            data = json.dumps(database, indent=4)
            datafile.write(data)
    elif engine == 'csv':
        if isinstance(database, dict):
            database = from_json_to_csv(database)
        with open('database.txt', 'w', newline='') as datafile:
            writer = csv.writer(datafile)
            writer.writerows(database)


def read_database() -> dict:
    """Чтение базы данных из файла.

    Вся работа с БД осуществялется как с объектом типа dict, поэтому в случае хранения данных в формате csv
    происходит конвертация прочтенной БД в словарь.
    """
    database = None
    with open('database.txt', 'r') as datafile:
        data = datafile.read()
        if data[0] == '{':
            database = json.loads(data)
        elif data:
            datafile.seek(0)
            reader = csv.reader(datafile)
            database = []
            for row in reader:
                database.append(row)
            database = from_csv_to_json(database)
        else:
            print("Can't read file.")
    return database


def from_json_to_csv(database: dict) -> list:
    """Конверация базы данных из JSON в CSV.

    Конвертация базы данных из объекта типа dict в объект типа list.
    """
    columns = ['Numbers', 'ID', 'First name', 'Last name', 'Birth date', 'Profession']
    data = [columns]
    for user_num, user in database.items():
        list = [user_num]
        for value in user.values():
            list.append(value)
        data.append(list)
    database = data
    return database


def from_csv_to_json(database: list) -> dict:
    """Конверация базы данных из CSV в JSON.

    Конвертация базы данных из объекта типа list в объект типа dict.
    """
    data = {}
    keys = database[0]
    for line in database[1:]:
        data[line[0]] = dict(zip(keys[1:], line[1:]))
    database = data
    return database


def choosing_database(engine: str) -> dict:
    """Инициация работы с БД

    Осуществляется выбор между созданием новой БД, либо работой в уже существующей БД. В обеих случаях идет перезапись
    данных в файл с учетом выбранного типа хранения данных.
    """
    print('\nChoose what you want:',
          '    1. create new database',
          '    2. work in exist database',
          sep='\n')
    while True:
        choice = input('Your choice (number): ')
        try:
            choice = int(choice)
        except ValueError:
            print('Incorrect input. Enter a number.')
        else:
            if choice == 1:
                database = create_database()
                write_database(database, engine)
                break
            elif choice == 2:
                try:
                    database = read_database()
                except FileNotFoundError:
                    print("Did't find the database. You have to create it.")
                else:
                    write_database(database, engine)
                    break
            else:
                print('Incorrect input. Enter only 1 or 2.')
    return database


def print_database_information(database: dict):
    """Вывод информации о БД.
    """
    database_size = len(database)
    print(f'\nSize of current database: {database_size} user(s).')
    for user, user_data in database.items():
        print(f'\n{user}:')
        for key, value in user_data.items():
            print(f'    {key}: {value}')


def printing_requirements():
    """Вывод требований к данным.

    Вывод требований к данным для ввода нового пользователя.
    """
    print('Requirements for entering parameters:',
          '    ID: 6 nums (only numbers);',
          '    First name: one word without numbers;',
          '    Last name: one word without numbers;',
          '    Birth date: format DD.MM.YYYY.\n',
          sep='\n')


def entering_new_user_info() -> dict:
    """Ввод данных для новой записи.

    Ввод данных новой записи с проверкой на корректность введенной информации.
    """
    header = ['ID', 'First name', 'Last name', 'Birth date', 'Profession']
    printing_requirements()
    header_for_input = [f'{name}:' for name in header]
    while True:
        user_info = list(map(input, header_for_input))
        if user_info[0].isdigit() and len(user_info[0]) == 6 and user_info[1].isalpha() and user_info[2].isalpha():
            try:
                datetime.strptime(user_info[3], '%d.%m.%Y')
            except ValueError:
                print('Incorrect format. Follow the requirements!\n')
                flag = breaking()
            else:
                user_info[1] = user_info[1].capitalize()
                user_info[2] = user_info[2].capitalize()
                user_info = dict(zip(header, user_info))
                break
        else:
            print('Incorrect format. Follow the requirements!\n')
            flag = breaking()
        if flag:
            user_info = None
            break
    return user_info


def finding_free_key(database: dict, size: int) -> int:
    """Поиск свободных ключей.

    Прим. В базе есть пользователи с ключами 1, 2, 5, 7. Свободные ключи: 3, 4, 6. Возвращает минимальный свободный ключ.
    """
    used_keys = []
    for key in database.keys():
        used_keys.append(int(key.split()[0]))
    free_keys = set(list(range(1, size + 1))) - set(used_keys)
    if not free_keys:
        free_key = size + 1
    else:
        free_key = min(free_keys)
    return free_key


def create_new_user(database: dict):
    """Добавление новой записи в БД.

    Добавление новой записи в БД с учетом проверки на уникальность ID и полного совпадения данных в записях.
    """
    print('\nTo create new user, you should enter all information about new user.')
    while True:
        new_user = entering_new_user_info()
        if new_user is not None:
            size = len(database)
            free_key = finding_free_key(database, size)
            key = f'{free_key} user'
            for user_data in database.values():
                if new_user['ID'] == user_data['ID']:
                    print('\nEntered ID already exist.')
                    flag = breaking()
                    break
                elif list(new_user.values())[1:] == list(user_data.values())[1:]:
                    print('\nEntered user already added.')
                    flag = breaking()
                    break
            else:
                database[key] = new_user
                print('\nNew user successfully added!')
                break
        else:
            print('You change your mind about creating new user.')
            break
        if flag:
            print('You change your mind about creating new user.')
            break
    return database


def choosing_criteria():
    """Выбор критерия.

    Выбор атрибута записи для дальнейшей работы с ним.
    """
    header = ['ID', 'First name', 'Last name', 'Birth date', 'Profession']
    criteria_numbers = list(range(1, len(header) + 1))
    criteria_numbers = list(map(str, criteria_numbers))
    criteria = dict(zip(criteria_numbers, header))
    print('\nChoose the criteria:',
          '    1. ID;',
          '    2. first name;',
          '    3. last name;',
          '    4. birth date;',
          '    5. profession.\n',
          sep='\n')
    while True:
        choice = input('Your choice (number): ')
        if choice in criteria:
            break
        else:
            print('There is no such criterion. Try again.')
    return criteria, choice


def filter_users(database: dict):
    """Фильтр записей.

    Фильтр записей в БД по выбранному критерию. Фильтр работает путем поиска совпадения искомой информации c информацией
    по выбранному критерию в записях БД.
    """
    while True:
        criteria, choice = choosing_criteria()
        criterion = criteria[choice]
        finding_value = input('Enter the value for the criterion: ')
        users_data = list(database.values())
        users_numbers = list(database.keys())
        filtered_database = {users_numbers[ind]: user for ind, user in enumerate(users_data)
                             if user.get(criterion) == finding_value}
        if not filtered_database:
            print('\nThere are no users with such filter options.')
            flag = breaking()
            if flag:
                break
        else:
            filtered_database_size = len(filtered_database)
            print(f'\n{filtered_database_size} user(s) could be found.')
            for user, user_data in filtered_database.items():
                print(f'\nUser number in database: {user}')
                for key, value in user_data.items():
                    print(f'    {key}: {value}')
            break


def finding(database: dict) -> str:
    """Поиск записи по ID.

    Поиск записи по ID для дальнейше работы с ней.
    """
    while True:
        user = None
        id = input('Enter the ID: ')
        for user, user_data in database.items():
            if user_data['ID'] == id:
                print(f'\n{user}:')
                for key, value in user_data.items():
                    print(f'    {key}: {value}')
                flag = True
                break
        else:
            print('\nThere are no users with such ID.')
            flag = breaking()
        if flag:
            break
    return user


def find_user(database: dict):
    """Поиск записи по ID.

    Поиск записи по ID и ее вывод.
    """
    print('\nEnter ID to find user.')
    finding(database)


def delete_user(database: dict) -> dict:
    """Удаление записи по ID.
    """
    print('\nEnter ID to delete user.')
    user_to_delete = finding(database)
    deleted_user_id = database[user_to_delete]['ID']
    del database[user_to_delete]
    print(f'\nUser {deleted_user_id} successfully deleted.')
    return database


def edit_user(database: dict) -> dict:
    """Редактирование записи в БД.

    Редактирование записи в БД с проверкой на корректность введенной информации.
    """
    print('\nEnter ID to edit user.')
    user_to_edit = finding(database)
    criteria, choice = choosing_criteria()
    choice = criteria[choice]
    print('Remember about requirements!')
    printing_requirements()
    flag = None
    while True:
        new_value = input(f'Enter new value for {choice}: ')
        if choice == criteria['1'] and new_value.isdigit() and len(new_value) == 6:
            break
        elif choice == criteria['2'] or choice == criteria['3'] and new_value.isalpha():
            new_value = new_value.capitalize()
            break
        elif choice == criteria['4']:
            try:
                datetime.strptime(new_value, '%d.%m.%Y')
            except ValueError:
                print('Incorrect format. Follow the requirements!\n')
                flag = breaking()
                if flag:
                    break
            else:
                break
        elif choice == criteria['5']:
            break
        else:
            flag = breaking()
            if flag:
                break
    if not flag:
        database[user_to_edit][choice] = new_value
        print(f'\n{user_to_edit}:')
        for key, value in database[user_to_edit].items():
            print(f'    {key}: {value}')
    else:
        print('You change your mind about creating new user.')
    return database


def exit_from(database: dict) -> bool:
    """Выход из БД.
    """
    print()
    options = ['Y', 'N']
    while True:
        flag = None
        check = input('Are you sure you saved the database (Y/N)? ').upper()
        if check == 'Y':
            break
        elif check == 'N':
            while True:
                check = input('You want to save the database (Y/N)? ').upper()
                if check == 'Y':
                    saving(database)
                    flag = True
                    break
                elif check == 'N':
                    flag = True
                    break
                else:
                    print('Only "Y" or "N". Try again')
        else:
            print('Only "Y" or "N". Try again')
        if flag:
            break
    flag = None
    while True:
        check = input('You really want to exit (Y/N)? ').upper()
        if check in options:
            break
    if check == 'Y':
        print('\nFarewell, my dear friend.')
        flag = True
    else:
        print("\nOk. Let's continue.")
    return flag


def saving(database: dict):
    """Сохранение БД.

    Сохранение БД с учетом выбранного типа хранения данных.
    """
    write_database(database, engine)
    print('Database has been saved!')


def breaking() -> bool:
    """Прерывание действия.

    Используется во время некорректного ввода информации для выхода из цикла ввода информации.
    """
    print('What would you like to do?',
          '    1. try again;',
          '    2. exit.',
          sep='\n')
    flag = None
    while True:
        choice = input('Your choice (number): ')
        if choice == '2':
            flag = True
            break
        elif choice == '1':
            print('')
            break
        else:
            print('Incorrect input. Try again.')
    return flag
