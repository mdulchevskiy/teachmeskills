# В массиве целых чисел с количеством элементов 19. Определить
# максимальное число и заменить им все четные по значению элементы.


my_array = [3, 2, 5, 6, 13, 18, 7, 4, 53, 12, 13, 72, 1, 8, 15, 16, 21, 22, 19]
print(my_array)
max_num = my_array[0]
for elem in my_array:
    if elem > max_num:
        max_num = elem

for i, elem in enumerate(my_array):
    if not elem % 2:
        my_array[i] = max_num
print(my_array)
