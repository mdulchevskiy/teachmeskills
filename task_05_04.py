# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
# [02-3.2-ML21]


n = input('Enter the number: ')
if n.isdigit():
    n_int = int(n)
    n_sum = 0
    for i in range(1, n_int + 1):
        n_sum += 1 / i
    print(f'S=1+1/2+1/3+1/4+...+1/N for N = {n_int} is {n_sum}')
else:
    print('You entered incorrect number. Try again.')
