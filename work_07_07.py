# Создать функцию, которая принимает на вход неопределенное количество именных
# аргументов и выводит на экран те из них, длина ключа которых четная.


def my_func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(f'Key ({key}), value ({value}).')


my_func(max=3, min=2, mode=4, nano='max')
