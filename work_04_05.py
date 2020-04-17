# Написать программу, которая будет выводить на экран случайные числа
# от 1 до 10 до тех пор, пока не выпадет 7.


from random import randint


i = 1
while True:
    random_number = randint(1, 10)
    print(random_number)
    if random_number == 7:
        break
    i += 1
print(f'Counter is {i}')
