# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1), и False
# в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
# ных чисел. С помощью функции is_power_n найти количество степеней чис-
# ла N в данном наборе.
# [01-11.2-Proc17]


def is_power_n(k, n):
    while k > 1:
        k /= n
    if k == 1:
        return True


def main():
    n = 2
    int_nums = [1, 2, 4, 5, 1024, 1025, 8, 16, 7, 3]
    pow_nums = []
    for num in int_nums:
        if is_power_n(num, n):
            count = 0
            while not num == 1:
                num /= n
                count += 1
            pow_nums.append(count)
        else:
            pow_nums.append(None)
    print(int_nums)
    print(pow_nums)


if __name__ == '__main__':
    main()
