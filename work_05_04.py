# Дана целочисленная матрица А[n,m]. Посчитать количество элементов матрицы, превосходящих
# среднее арифметическое значение элементов матрицы и сумма индексов которых четна.
# [02-4.2-BL23]


from random import randint


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
matrix_a = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(randint(0, 16))
    matrix_a.append(line)
print(f'\nMatrix = {matrix_a}')

m_sum = 0
count1 = 0
for line in matrix_a:
    for elem in line:
        m_sum += elem
        count1 += 1
m_mean = m_sum / count1
print(f'Matrix mean = {m_mean}\n')

count2 = 0
for i, line in enumerate(matrix_a):
    for j, elem in enumerate(line):
        if elem > m_mean and not (i + j) % 2:
            count2 += 1
            print(f'[{i}][{j}] - {elem}')
print(f'Number of elements is {count2}')
