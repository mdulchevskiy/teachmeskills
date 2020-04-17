# Составить список чисел Фибоначчи содержащий 15 элементов. Подсказка:
# Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8.
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла while,
# другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.


print('Solution with "for":')
for_fib_list = [1, 1]
for i in range(2, 16):
    for_fib_list.append(for_fib_list[-1] + for_fib_list[-2])
print(f'Solution with "for": {for_fib_list}')

print('\nSolution for "while":')
while_fib_list = [1, 1]
while len(while_fib_list) < 16:
    while_fib_list.append(while_fib_list[-1] + while_fib_list[-2])
print(f'Solution for "while": {while_fib_list}')
