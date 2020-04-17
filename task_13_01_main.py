# Написать калькулятор. Программа должна содержать 4 функции
# принимающие два аргумента и возвращающие результаты сложения,
# вычитания, умножения и деления. Реализовать пользовательский интерфейс
# с бесконечным циклом. Добавить валидацию входных данных. Программа
# должна состоять из четырех файлов(main.py, func.py, ui_func.py exceptions.py).


from task_13_01_ui_func import operation_choosing, numbers_entering


def main():
    while True:
        numbers = numbers_entering()
        operation_func = operation_choosing()
        if operation_func is None:
            break
        print(f'\nThe result: {operation_func(*numbers)}\n')


if __name__ == '__main__':
    main()
