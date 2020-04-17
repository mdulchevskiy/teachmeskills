# Написать калькулятор с использованием класса Math. Класс принимает
# в качестве аргументов два числа. Определить 4 метода (сложение, вычитание, умножение, деление).
# Реализовать пользовательский интерфейс с бесконечным циклом. Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов (main.py, classes.py, ui_func.py exceptions.py).


from task_13_02_exceptions import number_input_validation, operation_input_validation
from task_13_02_classes import Math


def numbers_entering():
    print('Enter two numbers.')
    a = input('    enter "a": ')
    b = input('    enter "b": ')
    numbers = number_input_validation(a, b)
    if numbers is None:
        return numbers_entering()
    else:
        return numbers


def operation_choosing(numbers):
    print('\nChoose the operation:',
          '    0. Exit;',
          '    1. Addition;',
          '    2. Subtraction;',
          '    3. Multiplication;',
          '    4. Division.',
          sep='\n')
    operation_dict = {1: 'addition',
                      2: 'subtraction',
                      3: 'multiplication',
                      4: 'division'}
    operation = input('Enter the number of operation: ')
    operation = operation_input_validation(operation)
    if operation is None:
        return operation_choosing(numbers)
    elif not operation:
        return None
    else:
        return getattr(numbers, operation_dict[operation])
