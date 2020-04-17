# Введите число. Если это число делится на 1000
# без остатка, то выведите на экран "millennium"


while True:
    my_numb = input('Input number = ')
    if my_numb.isdigit():
        break
    print('Incorrect input. Try again.')
if int(my_numb) % 1000 == 0:
    print("millennium")
