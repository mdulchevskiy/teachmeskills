# Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
# Определить конструктор с параметрами(передача размерности: n, m и диапазона случайных чисел:
# a, b). По-умолчанию(матрица 5 на 5 где все элементы равны нулю). Переопределить магический метод
# __str__ для красивого вывода. Описать функции, которые принимают на вход объект класса Matrix.
# Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами.


def matrix_max_elem(matrix):
    max_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem > max_elem:
                max_elem = elem
    return max_elem


def matrix_min_elem(matrix):
    min_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem < min_elem:
                min_elem = elem
    return min_elem


def matrix_sum(matrix):
    summ = 0
    for line in matrix.data:
        for elem in line:
            summ += elem
    return summ
