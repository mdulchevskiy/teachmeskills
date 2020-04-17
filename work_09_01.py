# Создать lambda функцию, которая принимает на
# вход имя и выводит его в формате “Hello, {name}”.


def main():
    my_func = lambda name: f'Hello, {name}!'
    print(my_func('Max'))


if __name__ == '__main__':
    main()
