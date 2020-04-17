# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.


from random import randint


n = int(input('Enter n: '))
my_matrix = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(randint(1, 10))
    my_matrix.append(line)
print(my_matrix)
