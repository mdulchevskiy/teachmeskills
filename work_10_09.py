# Использовать результаты 10.8. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в task_10_09.py.
# a)Создать функцию подсчета полной суммы всех товаров.
# b)Создать функцию поиска самого дорогого товара.
# c)Создать функцию самого дешевого товара.
# d)Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)


from csv_utils import (read_csv,
                       product_sum,
                       find_expensive,
                       find_cheap,
                       del_lines_from_csv,
                       write_csv)


def main():
    filename = 'work_10_08.txt'
    fields, rows = read_csv(filename)
    print(fields)
    for line in rows:
        print(line)

    write_csv('work_10_09.txt', fields, rows)
    filename = 'work_10_09.txt'

    price1, item1 = find_expensive(rows)
    price2, item2 = find_cheap(rows)
    n = 3
    print(f'\na) Full sum is {product_sum(rows)}')
    print(f'b) The biggest cost is {price1} for {item1}')
    print(f'c) The cheapest good is {item2} with price {price2}')
    print(f'd) The result of deleting {n} items:')
    del_lines_from_csv(filename,n)
    fields, rows = read_csv(filename)
    print(f'\n{fields}')
    for line in rows:
        print(line)


if __name__ == '__main__':
    main()
