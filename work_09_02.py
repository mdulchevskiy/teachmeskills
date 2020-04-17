# Создать lambda функцию, которая принимает на вход список имен
# и выводит их в формате “Hello, {name}” в другой список.


def main():
    my_func = lambda name_list: [f'Hello, {name}!' for name in name_list]
    name_list = ['Max', 'Kate', 'Mick']
    print(my_func(name_list))


if __name__ == '__main__':
    main()
