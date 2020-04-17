# Дано число. Найти сумму и произведение его цифр.


my_num = input('Enter the number: ')
if my_num.isdigit():
    digit_list = list(my_num)
    digit_sum = 0
    digit_prod = 1
    for digit in digit_list:
        digit_int = int(digit)
        digit_sum += digit_int
        digit_prod *= digit_int
    print(f'The product of digits in number {my_num} is {digit_prod}\n'
          f'The sum of digits in number {my_num} is {digit_sum}')
else:
    print('Incorrect input.')
