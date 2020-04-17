# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа ({‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys(). Подсказка: создается
# новый ключ с цифрой в конце, старый удаляется. Примечание: во всех задачах предоставить
# 2 решения. Одно с использованием цикла while, другое с использованием цикла for с
# параметром. Оба решения предоставить в одном файле.


my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

print('Solution with "for":')
print(f'Old dict: {my_dict}')
old_keys = list(my_dict.keys())
for key in old_keys:
    new_key = f'{key}{len(key)}'
    my_dict[new_key] = my_dict.pop(key)
print(f'New dict: {my_dict}')

print('\nSolution for "while":')
print(f'Old dict: {my_dict}')
old_keys = list(my_dict.keys())
index = 0
length = len(old_keys)
while index < length:
    new_key = f'{old_keys[index]}{len(old_keys[index])}'
    my_dict[new_key] = my_dict.pop(old_keys[index])
    index += 1
print(f'New dict: {my_dict}')
