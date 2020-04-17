# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить:
# You are the loser и правильное число.


from random import randint


start_range = int(input('Guess from: '))
stop_range = int(input('Guess to: '))
try_amount = int(input('Amount of try: '))

mystery_int = randint(start_range,stop_range)
count = 0
while True:
    int_try = int(input('Enter the number: '))
    count += 1
    if count == try_amount:
        print(f'Game over. Mystery int is {mystery_int}')
        break
    else:
        if mystery_int > int_try:
            print('Mystery int more than yours int')
        elif mystery_int < int_try:
            print('Mystery int less than yours int')
        else:
            print('You are the winner')
