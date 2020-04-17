# Описать функцию Sin1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0),
# находящую приближенное значение функции sin(x):
# sin(x) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Sin1 найти
# приближенное значение синуса для данного x при шести данных ε.
# [01-11.3-Proc41]


def sin1(x, eps):
    sinx = x
    count = 1
    part = None
    while part is None or abs(part) > eps:
        factorial = 1
        for num in range(1, 2 * count + 2):
            factorial *= num
        part = ((-1) ** count) * ((x ** (2 * count + 1)) / factorial)
        sinx += part
        count += 1
    return sinx


def main():
    x = 3
    eps = [0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
    for epsilon in eps:
        print(f'Sin({x}) with accuracy {epsilon} is {sin1(x,epsilon)}')


if __name__ == '__main__':
    main()
