# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку
# данных - удалять все четные элементы из списка.


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def deleting(num_list):
        num_list = list(filter(lambda num: num % 2, num_list))
        result = func(num_list)
        return result

    return deleting


@my_decorator
def num_list_printing(num_list):
    return num_list


def main():
    print(num_list_printing([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()
