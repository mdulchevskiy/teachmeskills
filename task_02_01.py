# Создать строку равную третьему символу введенной строки.


while True:
    my_string = input('Введите любую строку (не менее 3-х символов): ')
    if len(my_string) >= 3:
        break
    else:
        print('Строка содержит менее 3-х символов. Попробуйте еще раз.')
my_string_slice = my_string[2]
print('Третий символ введенной строки: ', my_string_slice)
