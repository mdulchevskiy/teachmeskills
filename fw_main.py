# Создать программу для работы с  учетными записями пользователей.
# Программа позволяет создавать, искать, править, фильтровать, удалять.
# Учетная запись пользователя представляет из себя словарь со следующими
# данными: имя, фамилия, дата рождения, профессия, числовой идентификатор(id).
# Пользователь может выбирать, каким образом будут храниться данные: в csv, либо в json.


from funcs import (choosing_database,
                   print_database_information,
                   create_new_user,
                   filter_users,
                   saving,
                   exit_from,
                   find_user,
                   delete_user,
                   edit_user,
                   engine_settings)


def main():
    engine = engine_settings()
    user_database = choosing_database(engine)
    while True:
        actions = dict([(1, print_database_information),
                        (2, create_new_user),
                        (3, delete_user),
                        (4, find_user),
                        (5, edit_user),
                        (6, filter_users),
                        (7, saving)])
        number_of_actions = len(actions)
        print('------------------------------------------------------')
        print('*To see supported actions for database enter "actions"*')
        action = input('Enter what you want to do: ')

        if action == 'actions':
            print('\nSupported actions for database:',
                  '    1) enter 0 to exit;',
                  '    2) enter 1 to see an information about database;',
                  '    3) enter 2 to create new user;',
                  '    3) enter 3 to delete user by ID;',
                  '    4) enter 4 to find user by ID;',
                  '    5) enter 5 to edit user information;.',
                  '    6) enter 6 to filter users;',
                  '    7) enter 7 to save the database.',
                  sep='\n')
            continue
        elif not action.isdigit():
            print('Incorrect input. Try again.')
            continue
        action = int(action)
        database = None
        if not action:
            flag = exit_from(user_database)
            if flag:
                break
        elif action > number_of_actions:
            print('There is no such action. Look at the "actions" and try again.')
        else:
            action_func = actions[action]
            database = action_func(user_database)
        if database:
            user_database = database


if __name__ == '__main__':
    main()
