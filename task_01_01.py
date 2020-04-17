# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.


while True:
    print('Введите 2 действительных числа a и b:')
    try:
        a = int(input('a = '))
        b = int(input('b = '))
    except ValueError:
        print('Некорректный ввод. Повторите попытку.')
    else:
        break
print('Сумма a и b равна: ', a + b)
print('Разность a и b равна: ', a - b)
print('Произведение a и b равно: ', a * b)
