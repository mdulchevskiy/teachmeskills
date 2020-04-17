# Задан целочисленный массив. Определить количество участков массива, на котором элементы
# монотонно возрастают (каждое следующее число больше предыдущего).
# [02-4.1-ML27]


numbers = [3, 2, 5, 6, 13, 18, 7, 6, 5, 4, 53, 12, 13, 72, 1, 8, 15, 16, 21, 22, 19]
print(numbers)
length = len(numbers)
amount = 0
is_same = False
for i in range(1, length):
    if numbers[i] > numbers[i - 1] and not is_same:
        amount += 1
        is_same = True
    else:
        if numbers[i] <= numbers[i - 1]:
            is_same = False
print(amount)
