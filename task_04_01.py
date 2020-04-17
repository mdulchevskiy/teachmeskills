# Дан список целых чисел. Создать новый список, каждый элемент которого равен
# исходному элементу умноженному на -2. Примечание: во всех задачах предоставить
# 2 решения. Одно с использованием цикла while, другое с использованием цикла
# for с параметром. Оба решения предоставить в одном файле.


my_list = [1, 12, 23, 21, 45, 2, 5, 76, 8, 9, 40, 82]

print('Solution with "for":')
new_list = []
for i in my_list:
    new_list.append(i * -2)
print(f'Old list: {my_list}\nNew list: {new_list}')

print('\nSolution for "while":')
new_list = []
index = 0
length = len(my_list)
while index < length:
    new_list.append(my_list[index] * -2)
    index += 1
print(f'Old list: {my_list}\nNew list: {new_list}')
