# Создать универсальный декоратор, который меняет порядок аргументов
# в функции на противоположный.


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = args[::-1]
        result = func(*args, **kwargs)
        return result

    return wrapper


@my_decorator
def my_print_list(*args):
    for i, arg in enumerate(args):
        print(f'index {i}: {arg}')


def main():
    my_print_list(1, 2, 3, 4, 5, 6)


if __name__ == '__main__':
    main()
