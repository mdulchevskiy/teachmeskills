# Создать функцию, которая принимает на вход неопределенное
# количество аргументов и возвращает их сумму и максимальное из них.


def strange_func(*args):
    arg_sum = 0
    max_arg = args[0]
    for elem in args:
        arg_sum += elem
        if elem > max_arg:
            max_arg = elem
    return arg_sum, max_arg


arg_sum, max_sum = strange_func(1, 2, 3, 4)
print(arg_sum, max_sum)
