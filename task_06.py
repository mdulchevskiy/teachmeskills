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

# 7. Найти индекс ряда с минимальной суммой элементов.
min_row_sum = None
min_row_sum_index = None
for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j]
    if min_row_sum is None or min_row_sum > row_sum:
        min_row_sum = row_sum
        min_row_sum_index = i
print(min_row_sum_index)

# 8. Найти индекс колонки с минимальной суммой элементов.
min_column_sum = None
min_column_sum_index = None
for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += matrix[i][j]
    if min_column_sum is None or min_column_sum > column_sum:
        min_column_sum = column_sum
        min_column_sum_index = j
print(min_column_sum_index)

# 9. Обнулить все элементы выше главной диагонали.
for i in range(n):
    for j in range(m):
        if i < j:
            matrix[i][j] = 0
print(matrix)

# 10. Обнулить все элементы ниже главной диагонали.
for i in range(n):
    for j in range(m):
        if i > j:
            matrix[i][j] = 0
print(matrix)

# 11. Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.
matrix_a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(a, b))
    matrix_a.append(row)
print(matrix_a)

matrix_b = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(a, b))
    matrix_b.append(row)
print(matrix_b)

# 12. Создать матрицу равную сумме matrix_a и matrix_b.
sum_matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    sum_matrix.append(row)
print(sum_matrix)
