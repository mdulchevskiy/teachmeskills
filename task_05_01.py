# Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный
# знак операции, а также на ввод Y=0 при делении. Организовать возможность многократных вычислений
# без перезагрузки программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').


signs = ['+', '-', '/', '*']
print('To escape from calculating enter the 0 in sign.\n')
while True:
    x = input('Enter the number X: ')
    y = input('Enter the number Y: ')
    sign = input('Enter the sign (+,-,/,*): ')
    if x.isdigit() and y.isdigit():
        if sign == '0':
            break
        elif sign in signs:
            int_x = int(x)
            int_y = int(y)
            if sign == '/' and not int_y:
                print('Cannot divide by zero.\n')
                continue
            str_operation = f'{int_x} {sign} {int_y}'
            z = eval(str_operation)
            print(f'\nThe result of "{str_operation}" is {z}\n')
        else:
            print('\nYou entered incorrect sign. Try again '
                  'and enter any sign from these ones: +, -, /, *.\n')
    else:
        print('\nYou entered incorrect numbers. Try again.\n')
