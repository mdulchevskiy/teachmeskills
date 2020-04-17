# Имеется текстовый файл. Все четные строки этого
# файла записать во второй файл, а нечетные — в
# третий файл. Порядок следования строк сохраняется.


def main():
    with open('work_10_05_orig.txt') as input_file:
        with open('work_10_05_even.txt','w') as even_file:
            with open('work_10_05_odd.txt','w') as odd_file:
                lines = input_file.readlines()
                for i, line in enumerate(lines):
                    if not (i + 1) % 2:
                        even_file.write(line)
                    else:
                        odd_file.write(line)

    print('*** Original ***')
    with open('work_10_05_orig.txt', 'r') as my_file:
        while True:
            line = my_file.readline()
            if not line:
                break
            else:
                print(line.strip())

    print('\n*** Even ***')
    with open('work_10_05_even.txt', 'r') as my_file:
        while True:
            line = my_file.readline()
            if not line:
                break
            else:
                print(line.strip())

    print('\n*** Odd ***')
    with open('work_10_05_odd.txt', 'r') as my_file:
        while True:
            line = my_file.readline()
            if not line:
                break
            else:
                print(line.strip())


if __name__ == '__main__':
    main()
