# Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
# Определить конструктор с параметрами(передача размерности: n, m и диапазона случайных чисел:
# a, b). По-умолчанию(матрица 5 на 5 где все элементы равны нулю). Переопределить магический метод
# __str__ для красивого вывода. Описать функции, которые принимают на вход объект класса Matrix.
# Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами.


from random import randint


class Matrix:
    def __init__(self, *args):
        if len(args) == 4:
            self.n, self.m, a, b = args
            self.data = [[randint(a, b) for i in range(self.n)] for j in range(self.m)]
        elif len(args) == 1 and isinstance(args[0], Matrix):
            source_matrix = args[0]
            self.n = source_matrix.n
            self.m = source_matrix.m
            self.data = source_matrix.data
        else:
            self.n = 5
            self.m = 5
            self.data = [[0 for i in range(self.n)] for j in range(self.m)]

    def __str__(self):
        result_line = ""
        for i, line in enumerate(self.data):
            str_line = ' '.join(map(str, line))
            result_line += f'{str_line}\n'
        return result_line
