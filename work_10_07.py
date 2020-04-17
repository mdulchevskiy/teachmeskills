# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл


from random import randint
import json


def create_matrix(n):
    matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
    return matrix


def write_json_file(data, filename):
    with open(filename, 'w') as write_file:
        json_data = json.dumps(data)
        write_file.write(json_data)


def read_json_file(filename):
    with open(filename) as read_file:
        data = json.loads(read_file.read())
    return data


def make_zero_even_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if not elem % 2:
                matrix[i][j] = 0


def main():
    first_file_name = 'work_10_07_01.json'
    second_file_name = 'work_10_07_02.json'

    matrix = create_matrix(5)
    write_json_file({'matrix': matrix}, first_file_name)

    data = read_json_file(first_file_name)
    matrix = data['matrix']
    make_zero_even_matrix(matrix)
    write_json_file({'matrix': matrix}, second_file_name)


if __name__ == '__main__':
    main()
