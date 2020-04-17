# Описать функцию fact2(n) вещественного типа, вычисляющую двойной факториал:
# n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное
# (n > 0 — параметр целого типа). С помощью этой функции найти двойные факториалы
# пяти данных целых чисел.
# [01-11.2-Proc35]


def fact2(n):
    factorial = 1
    start = 2 if not n % 2 else 3
    for i in range(start, n + 1, 2):
        factorial *= i
    return factorial


def main():
    numbers = [5, 6, 4, 8, 9, 1, 2, 3, 4]
    for num in numbers:
        print(f'{num}!! is {fact2(num)}')


if __name__ == '__main__':
    main()
