# Дан двумерный массив n × m элементов. Определить, сколько раз
# встречается число 7 среди элементов массива.
# [02-4.2-BL12]


from random import randint


n = int(input('Rows: '))
m = int(input('Columns: '))
matrix_a = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(randint(0, 16))
    matrix_a.append(line)
print(matrix_a)

count = 0
for line in matrix_a:
    for elem in line:
        if elem == 7:
            count += 1
print(count)
