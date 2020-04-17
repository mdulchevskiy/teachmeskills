# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать
# функцию. Подсказка: для хранения данных использовать словарь. Для проверки
# нахождения элемента в словаре использовать метод get(), либо оператор in.


def calculation(numbers):
    my_dict = {}
    for number in numbers:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    print(my_dict)


def main():
    my_list = [1, 2, 4, 5, 6, 1, 1, 5, 4]
    calculation(my_list)


if __name__ == '__main__':
    main()
