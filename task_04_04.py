# Дан список. Создать новый список, сдвинутый на 1 элемент влево.
# Пример: 1 2 3 4 5 ->  2 3 4 5 1. Примечание: во всех задачах предоставить 2 решения.
# Одно с использованием цикла while, другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Solution with "for":')
new_list = []
length = len(my_list)
for i in range(length):
    new_list.append(my_list[i-1])
print(f'Old list: {my_list}\nNew list: {new_list}')

print('\nSolution for "while":')
new_list = []
index = 0
length = len(my_list)
while index < length:
    new_list.append(my_list[index-1])
    index += 1
print(f'Old list: {my_list}\nNew list: {new_list}')

# решение без цикла
easy_new_list = my_list[1:]
easy_new_list.append(my_list[0])
print(easy_new_list)
