# Создать скрипт, который принимает имя папки
# и создает ее рядом со скриптом


from os.path import abspath, dirname
from os import mkdir


def main():
    folder_name = 'Test folder'
    current_path = abspath(__file__)
    dir_name = dirname(current_path)
    try:
        mkdir(f'{dir_name}/{folder_name}')
    except FileExistsError:
        print(f'Folder with name "{folder_name}" already exist.')


if __name__ == '__main__':
    main()
