# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.


from random import randint


n = 3
matrix_a = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(randint(0, 16))
    matrix_a.append(line)
print(matrix_a)

sum = 0
for i in range(n):
    for j in range(n):
        if not matrix_a[i][j] % 3:
            sum += matrix_a[i][j]
print(sum)
