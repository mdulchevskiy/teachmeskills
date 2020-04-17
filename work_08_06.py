# Написать функцию по решению квадратных уравнений.
# [01-11.2-Proc17]


from typing import Union


def quadratic(a: Union[int, float], b: int, c: int) -> tuple:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:
        x1, x2 = 0, 0
    return x1, x2


def main():
    x = quadratic(2, 3, 1)
    print(x)


if __name__ == '__main__':
    main()
