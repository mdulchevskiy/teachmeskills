# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.


def print_first_line(file_name):
    my_file = open(file_name)
    line = my_file.readline()
    if line:
        print(line.strip())
    else:
        print('File is empty')
    my_file.close()


def print_fifth_line(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            print('File size is less than 5')
            break
        if i + 1 == 5:
            print(f'The 5th line: {line.strip()}')
            break
        i += 1
    my_file.close()


def print_first_five_lines(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            print('File size is less than 5')
            break
        if i >= 5:
            break
        i += 1
        print(f'Line #{i:02}: {line.strip()}')
    my_file.close()


def print_lines_from_s1_to_s2(file_name, s1, s2):
    my_file = open(file_name)
    i = 0
    if s1 > s2:
        print('Bad input')
        return
    while True:
        line = my_file.readline()
        if not line:
            break
        if s1 <= i + 1 <= s2:
            print(f'Line #{i+1:02}: {line.strip()}')
        i += 1
    my_file.close()


def print_entire_file(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            break
        i += 1
        print(f'Line #{i:02}: {line.strip()}')
    my_file.close()


def main():
    print('a)')
    print_first_line('work_10_01.txt')
    print('\nb)')
    print_fifth_line('work_10_01.txt')
    print('\nc)')
    print_first_five_lines('work_10_01.txt')
    print('\nd)')
    print_lines_from_s1_to_s2('work_10_01.txt', 2, 4)
    print('\ne)')
    print_entire_file('work_10_01.txt')


if __name__ == '__main__':
    main()
