# Дан список чисел. Вернуть список, где каждый число
# переведено в строку [5, 3] -> [‘5’, ‘3’].


def main():
    num_list = [1, 2, 3, 4, 5]
    str_list = list(map(str, num_list))
    print(str_list)


if __name__ == '__main__':
    main()
