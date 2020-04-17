# Создать текстовый файл и записать в него 3 строки.
# Записываемые строки вводятся с клавиатуры.


def main():
    with open('work_10_02.txt', 'w') as my_file:
        for _ in range(3):
            my_file.write(f'{input("line: ")}\n')
    with open('work_10_02.txt', 'r') as my_file:
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
