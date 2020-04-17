# Имеется текстовый файл. Переписать в другой файл все его строки
# с заменой в них символа 0 на символ 1 и наоборот.


def main():
    new_lines = []
    with open('work_10_04.txt', 'r') as my_file:
        old_lines = my_file.readlines()
        for ind, old_line in enumerate(old_lines):
            print(f'Line {ind+1}: {old_line.strip()}')
            new_line = ''
            for char in old_line:
                new_line += '0' if char == '1' else '1' if char == '0' else char
            new_lines.append(new_line)

    with open('work_10_04.txt', 'w') as my_file:
        my_file.writelines(new_lines)

    print('\n*** New book ***\n')

    with open('work_10_04.txt', 'r') as my_file:
        i = 1
        while True:
            line = my_file.readline()
            if not line:
                break
            else:
                print(f'Line {i}: {line.strip()}')
            i += 1


if __name__ == '__main__':
    main()
