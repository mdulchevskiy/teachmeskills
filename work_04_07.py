# Ввести два целых числа A и B ( A < B ). Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B ), а также количество N этих чисел.
# [01-08-For2]


a = int(input('A: '))
b = int(input('B: '))
counter = 0
for i in range(a, b + 1):
    counter += 1
    print(i)
print(f'amount is {counter}')
