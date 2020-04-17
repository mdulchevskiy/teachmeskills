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

# 5. Найти индекс ряда с максимальной суммой элементов.
max_row_sum = None
max_row_sum_index = None
for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j]
    if max_row_sum is None or max_row_sum < row_sum:
        max_row_sum = row_sum
        max_row_sum_index = i
print(max_row_sum_index)

# 6. Найти индекс колонки с максимальной суммой элементов.
max_column_sum = None
max_column_sum_index = None
for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += matrix[i][j]
    if max_column_sum is None or max_column_sum < column_sum:
        max_column_sum = column_sum
        max_column_sum_index = j
print(max_column_sum_index)
