# Создать функцию, принимающая на вход неопределенное
# количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10.


def strange_func(*args):
    summ = 0
    for elem, ind in enumerate(args):
        summ += elem * ind
    return summ


print(strange_func(4, 3, 2, 1))
