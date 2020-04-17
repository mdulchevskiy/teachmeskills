# Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а.


my_list = ['Dulchevskiy', 'Ustsimenlko', 'Петрова']
for second_name in my_list:
    if second_name[0] == 'П' and second_name[-1] == 'а':
        print(second_name)
