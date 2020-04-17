# Дан произвольный список, содержащий только числа.
# Выведите результат сложения всех чисел больше 10.


my_numbers = [16, 5, 40, 6, 7, 82, 9, 11, 23, 4, 5]
summ = 0
index = 0
length = len(my_numbers)

while index < length:
    if my_numbers[index] > 10:
        summ += my_numbers[index]
    index += 1
print(summ)
