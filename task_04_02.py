# Дан список целых чисел. Подсчитать сколько четных чисел в списке. Примечание:
# во всех задачах предоставить 2 решения. Одно с использованием цикла while,
# другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.


my_list = [1, 12, 23, 21, 45, 2, 5, 76, 8, 9, 40, 82]

print('Solution with "for":')
counter = 0
for i in my_list:
    if i % 2 == 0:
        counter += 1
print(f'{my_list}\nЧетных чисел {counter}')

print('\nSolution for "while":')
counter = 0
index = 0
length = len(my_list)
while index < length:
    if my_list[index] % 2 == 0:
        counter += 1
    index += 1
print(f'{my_list}\nЧетных чисел {counter}')
