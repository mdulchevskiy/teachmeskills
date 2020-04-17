# Модифицировать генератор, чтобы генератор принимал
# диапазон случайных чисел и чтобы последующее
# случайное число лежало в диапазоне смещенном на n.
# Пример: a = 1, b = 10, diff = 10
# 1. 1- 10
# 2. 11-20
# …
# N. N+10 - M+10


from random import randint
from time import sleep


def create_generator(a, b, diff):
    while True:
        yield randint(a, b)
        a += diff
        b += diff
        sleep(1)


def main():
    generator = create_generator(1, 9, 10)
    for num in generator:
        print(num)


if __name__ == '__main__':
    main()
