# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.
# [02-7.2-HL08]


my_str = input('Enter the line: ')
print(f'\nOriginal line: {my_str}.')
my_str_list = my_str.split()
my_str_list.reverse()
new_str = ' '.join(my_str_list)
print(f'Reversed line: {new_str}.')
