# Написать калькулятор. Программа должна содержать 4 функции
# принимающие два аргумента и возвращающие результаты сложения,
# вычитания, умножения и деления. Реализовать пользовательский интерфейс
# с бесконечным циклом. Добавить валидацию входных данных. Программа
# должна состоять из четырех файлов(main.py, func.py, ui_func.py exceptions.py).


def number_input_validation(*args):
    number_list = []
    for number in args:
        try:
            int(number)
        except ValueError:
            try:
                float(number)
            except ValueError:
                print('\nIncorrect input (must be int or float). Try again.\n')
                return None
            else:
                number = float(number)
                number_list.append(number)
        else:
            number = int(number)
            number_list.append(number)
    return number_list


def operation_input_validation(operation):
    try:
        operation = int(operation)
    except ValueError:
        print('\nIncorrect input (must be int). Try again.')
        return None
    else:
        if operation > 4 or operation < 0:
            print('\nIncorrect input (out of range). Try again.')
            return None
        return operation
