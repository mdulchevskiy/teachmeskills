# Просуммировать неопределенное количество чисел, вводимых пользователем.
# Суммировать до тех пор, пока пользователь не введёт слово «стоп».
# Не учитывать числа кратные 5.


summ = 0
while True:
    string = input('Enter some number: ')
    if string == 'stop':
        break
    elif not string.isdigit():
        print('Enter only numbers, Please')
        continue
    number = int(string)
    if number % 5 == 0:
        continue
    summ += number
print(summ)
