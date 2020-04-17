# Ввести строку. Если длина строки больше 10 символов, то создать
# новую строку с 3 восклицательными знаками в конце и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки


string = input('Enter string = ')
str_len = len(string)
if str_len > 10:
    string = f'{string}!!!'
elif str_len < 10:
    string = string[1]
print(string)
