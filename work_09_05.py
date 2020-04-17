# Дан список чисел. Найти произведение всех чисел, которые кратны 3.


from functools import reduce


def main():
    num_list = [1, 2, 3, 4, 5, 6, 7, 9]
    product = reduce(lambda a, num: a * num, filter(lambda num: not num % 3, num_list))
    print(product)


if __name__ == '__main__':
    main()
