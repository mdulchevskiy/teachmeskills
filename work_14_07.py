# Дописать скрипт. Программа принимает имя папки и имя файла с расширением.
# Создает папку и создает в ней файл. Если расширение файла py - записывает в файл следующее:
# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()


from os.path import abspath, dirname
from os import mkdir


def main():
    folder_name = input('Enter folder name: ')  # 'Test folder'
    file_name = input('Enter file name: ')      # 'Test file.txt', 'test_module.py'
    lines = ['def main():', '\n', 'pass'.rjust(8), '\n\n\n',
             'if __name__ == "__main__":', '\n', 'main()'.rjust(10), '\n']
    current_path = abspath(__file__)
    dir_name = dirname(current_path)
    try:
        mkdir(f'{dir_name}/{folder_name}')
    except FileExistsError:
        print(f'Folder with name "{folder_name}" already exist.')
    with open(f'{dir_name}/{folder_name}/{file_name}', 'w') as file:
        if file_name.endswith('.py'):
            file.writelines(lines)


if __name__ == '__main__':
    main()
