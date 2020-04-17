# Рассчитать значение х определив и использовав необходимую функции.
# [02-5.1-BL01]


def part_calc(elem):
    part = (elem ** 0.5 + elem) / 2
    return part


def main():
    args = [5, 12, 19]
    sum = 0
    for num in args:
        sum += part_calc(num)
    print(sum)


if __name__ == '__main__':
    main()
