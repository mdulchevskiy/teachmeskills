# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку


from random import randint
from time import sleep


def create_generator(a, b):
    while True:
        yield randint(a, b)
        sleep(1)


def main():
    generator = create_generator(1, 9)
    for num in generator:
        print(num)


if __name__ == '__main__':
    main()
