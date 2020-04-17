from random import randint


# 1. Функция для создания матрицы размерностью a на b с рандомными числами от c до d.
def create_matrix(a, b, c, d):
    matrix = []
    for i in range(a):
        line = []
        for j in range(b):
            line.append(randint(c, d))
        matrix.append(line)
    return matrix


# 2. Функция для вывода матрицы.
def printing_matrix(matrix):
    print('Matrix:')
    for line in matrix:
        print(line)


# 3. Функция для нахождения суммы всех элементов.
def matrix_sum(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return summ


# 4. Функция для нахождение максимального элемента матрицы.
def max_element(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem


# 5. Функция для нахождения минимального элемента матрицы.
def min_element(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


matrix_a = create_matrix(3, 3, 0, 9)
printing_matrix(matrix_a)
max = max_element(matrix_a)
min = min_element(matrix_a)
summ = matrix_sum(matrix_a)
print(f'Min element is {min}.\nMax element is {max}.\nSumm of elements is {summ}.')
