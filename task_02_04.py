# Создать строку равную введенной строке без последних двух символов.


while True:
    my_string = input('Введите любую строку (не менее 3-х символов): ')
    if len(my_string) >= 3:
        break
    else:
        print('Строка содержит менее 3-х символов. Попробуйте еще раз.')
my_string_slice = my_string[:-2]
print('Введенная строка без последних двух символов: ', my_string_slice)
