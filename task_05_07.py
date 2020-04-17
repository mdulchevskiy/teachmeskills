# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]


from random import randint


n = input('Enter the square matrix size: ')
if n.isdigit():
    print('Original matrix:')
    n_int = int(n)
    matrix = []
    for i in range(n_int):
        line = []
        for j in range(n_int):
            line.append(randint(0, 16))
        matrix.append(line)
        print(line)

    print('\nNew matrix:')
    for ind, line in enumerate(matrix):
        max_elem = max(line)
        max_ind = line.index(max_elem)
        matrix[ind][ind], matrix[ind][max_ind] = matrix[ind][max_ind], matrix[ind][ind]
        print(line)
else:
    print('Incorrect input. Try again.')
