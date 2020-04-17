# Просуммировать неопределенное количество чисел, вводимых пользователем.
# Суммировать до тех пор, пока пользователь не введёт слово «стоп».


summ = 0
while True:
    string = input('Enter some number: ')
    if string == 'stop':
        break
    elif not string.isdigit():
        print('Enter only numbers!')
        continue
    number = int(string)
    summ += number
print(summ)
