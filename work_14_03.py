# Создать скрипт, который при запуске принимает неопределенное
# количество аргументов и считает сумму тех из них, что являются цифрами.
# Пример: python test.py 1 2 3 4 a b 5 6 -->  21


import sys


def main():
    print(sys.argv)
    summ = 0
    for elem in sys.argv:
        if elem.isdigit():
            summ += int(elem)
    print(summ)


if __name__ == '__main__':
    main()
