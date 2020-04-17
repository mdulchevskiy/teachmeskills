# Написать калькулятор. Программа должна содержать 4 функции
# принимающие два аргумента и возвращающие результаты сложения,
# вычитания, умножения и деления. Реализовать пользовательский интерфейс
# с бесконечным циклом. Добавить валидацию входных данных. Программа
# должна состоять из четырех файлов(main.py, func.py, ui_func.py exceptions.py).


from task_13_01_func import addition, subtraction, multiplication, division
from task_13_01_exceptions import operation_input_validation, number_input_validation


def numbers_entering():
    print('Enter two numbers.')
    a = input('    enter "a": ')
    b = input('    enter "b": ')
    numbers = number_input_validation(a, b)
    if numbers is None:
        return numbers_entering()
    else:
        return numbers


def operation_choosing():
    print('\nChoose the operation:',
          '    0. Exit;',
          '    1. Addition;',
          '    2. Subtraction;',
          '    3. Multiplication;',
          '    4. Division.',
          sep='\n')
    operation_dict = {1: addition,
                      2: subtraction,
                      3: multiplication,
                      4: division}
    operation = input('Enter the number of operation: ')
    operation = operation_input_validation(operation)
    if operation is None:
        return operation_choosing()
    elif not operation:
        return None
    else:
        return operation_dict[operation]
