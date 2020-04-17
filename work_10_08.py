# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле work_10_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.


from csv_utils import (read_csv,
                       write_csv,
                       add_to_csv,
                       del_line_from_csv)


def main():
    fields = ['Имя товара', 'Цена', 'Количество', 'Комментарий']
    rows = [
        ['Хлеб', '0.9', '3', 'черный'],
        ['Молоко', '1.3', '5', 'соевое'],
        ['Мясо', '6.4', '1.3', 'говдина'],
        ['Вода', '2.3', '2', 'спрайт'],
    ]
    filename = 'work_10_08.txt'
    write_csv(filename, fields, rows)

    new_fields, new_rows = read_csv(filename)
    print(new_fields)
    for line in new_rows:
        print(line)
    print('-------------------Добавление позиции---------------------')

    adding_rows = ['Чипсеки', '1.6', '56', 'на акции']
    add_to_csv(filename, adding_rows)
    new_fields, new_rows = read_csv(filename)
    print(new_fields)
    for line in new_rows:
        print(line)
    print('-------------------Удаление 3 строки----------------------')

    del_line_from_csv(filename, 3)
    new_fields, new_rows = read_csv(filename)
    print(new_fields)
    for line in new_rows:
        print(line)


if __name__ == '__main__':
    main()
