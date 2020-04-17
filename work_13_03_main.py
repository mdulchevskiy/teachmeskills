# Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
# Определить конструктор с параметрами(передача размерности: n, m и диапазона случайных чисел:
# a, b). По-умолчанию(матрица 5 на 5 где все элементы равны нулю). Переопределить магический метод
# __str__ для красивого вывода. Описать функции, которые принимают на вход объект класса Matrix.
# Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами.


from work_13_03_classes import Matrix
from work_13_03_funcs import (matrix_max_elem,
                              matrix_min_elem,
                              matrix_sum, )


def main():
    matrix1 = Matrix(4, 5, 1, 20)
    print(matrix1)
    print(f'Max elem: {matrix_max_elem(matrix1)}')
    print(f'Min elem: {matrix_min_elem(matrix1)}')
    print(f'Elems sum: {matrix_sum(matrix1)}')
    print()
    matrix2 = Matrix(matrix1)
    print(matrix2)
    matrix3 = Matrix()
    print(matrix3)


if __name__ == '__main__':
    main()
