# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.


def main():
    str_list = ['first string', 'second string', 'third string']
    new_str_list = [f'{ind} - {string}' for ind, string in enumerate(str_list)]
    print(str_list)
    print(new_str_list)


if __name__ == '__main__':
    main()
