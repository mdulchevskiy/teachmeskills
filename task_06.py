from random import randint


DEBUG = True

if DEBUG:
    n = 5
    m = 5
    a = 0
    b = 9
else:
    n = input('Enter n: ')
    m = input('Enter m: ')
    a = input('Enter a: ')
    b = input('Enter b: ')

# 1. Создать матрицу случайных чисел от a до b, размерность матрицы n*m.
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(a, b))
    matrix.append(row)
print(matrix)

# 2. Найти максимальный элемент матрицы.
max_elem = matrix[0][0]
for row in matrix:
    for elem in row:
        if elem > max_elem:
            max_elem = elem
print(max_elem)

# 3. Найти минимальный минимальный матрицы.
min_elem = matrix[0][0]
for row in matrix:
    for elem in row:
        if elem < min_elem:
            min_elem = elem
print(min_elem)

# 4. Найти сумму всех элементов матрицы.
summ = 0
for row in matrix:
    for elem in row:
        summ += elem
print(summ)
