# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки. Если нет, то получить
# номер первой строки, в которой эти файлы отличаются друг от друга.


def main():
    with open('work_10_06_01.txt') as file1, open('work_10_06_02.txt') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        for i in range(len(lines1)):
            if lines1[i] != lines2[i]:
                print(f'The difference in {i+1} line.')
                break
        else:
            print('Files are equal.')


if __name__ == '__main__':
    main()
