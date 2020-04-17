# Даны действительные числа x и y. Получить (|x|-|y|)/(1+|xy|)


while True:
    print('Введите 2 действительных числа x и y:')
    try:
        x = int(input('x = '))
        y = int(input('y = '))
    except ValueError:
        print('Некорректный ввод. Повторите попытку.')
    else:
        break
print('Результат: ', (abs(x) - abs(y)) / (1 + abs(x * y)))
