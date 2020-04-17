# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35


m_str = input('Enter m: ')
n_str = input('Enter n: ')
if m_str.isdigit() and n_str.isdigit():
    m = int(m_str)
    n = int(n_str)
    for num in range(m, n + 1):
        dividers = []
        right_border = num // 2 + 1
        for divider in range(2, right_border):
            if not num % divider:
                dividers.append(divider)
        print(f"{num}: {', '.join([str(item) for item in dividers])}")
else:
    print('You entered incorrect number. Try again.')
