# Написать декоратор, который будет выводить время выполнения функции.


from datetime import datetime, timedelta


def my_decorator(func):
    def time(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now() - start_time
        print(end_time)
        return result
    return time


@my_decorator
def my_func(a, b):
    return a + b


def main():
    print(my_func(3, 4))


if __name__ == '__main__':
    main()
