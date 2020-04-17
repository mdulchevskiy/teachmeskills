# Написать калькулятор с использованием класса Math. Класс принимает
# в качестве аргументов два числа. Определить 4 метода (сложение, вычитание, умножение, деление).
# Реализовать пользовательский интерфейс с бесконечным циклом. Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов (main.py, classes.py, ui_func.py exceptions.py).


from task_13_02_ui_func import numbers_entering, operation_choosing
from task_13_02_classes import Math


def main():
    while True:
        numbers = numbers_entering()
        numbers = Math(*numbers)
        result = operation_choosing(numbers)
        if result is None:
            break
        print(f'\nThe result: {result}\n')


if __name__ == '__main__':
    main()
