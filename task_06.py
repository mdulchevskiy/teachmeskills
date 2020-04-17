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
