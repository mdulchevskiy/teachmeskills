# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).


from random import randint


def create_matrix(n, c=1, d=9):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(randint(c, d))
        matrix.append(line)
    return matrix


matrix = create_matrix(3)
for line in matrix:
    print(line)
