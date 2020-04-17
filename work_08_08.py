# Дан массив целых чисел A. Найти суммы положительных
# и отрицательных элементов массива, используя функцию
# определения суммы.
# [02-5.1-BL21]


def calc_sum(numbers):
    pos_sum = 0
    neg_sum = 0
    for number in numbers:
        if number > 0:
            pos_sum += number
        elif number < 0:
            neg_sum += number
    return pos_sum, neg_sum


def main():
    numbers = [-1, 3, -5, 8, -14, 23, -4, 13, 11, 10, -10, -11]
    print(f'Sum of (positive numbers, negative numbers): {calc_sum(numbers)}')


if __name__ == '__main__':
    main()
