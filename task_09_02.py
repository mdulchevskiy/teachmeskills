# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной длины.
# {‘abc’: 5} -> {‘abcabc’: 5}


def main():
    my_lambda = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
    print(my_lambda(a='max', abc=5))


if __name__ == '__main__':
    main()
