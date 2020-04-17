# Дописать скрипт. Программа принимает имя папки и имя файла.
# Создает папку и создает в ней файл.


from os.path import abspath, dirname
from os import mkdir


def main():
    folder_name = 'Test folder'
    file_name = 'Test file.txt'
    current_path = abspath(__file__)
    dir_name = dirname(current_path)
    try:
        mkdir(f'{dir_name}/{folder_name}')
    except FileExistsError:
        print(f'Folder with name "{folder_name}" already exist.')
    with open(f'{dir_name}/{folder_name}/{file_name}', 'w') as file:
        pass


if __name__ == '__main__':
    main()
