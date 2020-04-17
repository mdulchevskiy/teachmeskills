# Написать функцию принимающая на вход неопределенное
# количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое
# либо среднегеометрическое. Написать программу в виде трех функций.


def geom_mean(*args):
    length = len(args)
    product = 1
    for num in args:
        product *= num
    result = product ** (1 / length)
    return result


def arifm_mean(*args):
    length = len(args)
    summ = 0
    for num in args:
        summ += num
    result = summ / length
    return result


def main_func(*args, mean_type):
    if mean_type == 'geom':
        return geom_mean(*args)
    elif mean_type == 'arifm':
        return arifm_mean(*args)


print(main_func(1, 2, 3, 4, mean_type='geom'))
print(main_func(1, 2, 3, 4, 5, 6, mean_type='arifm'))
