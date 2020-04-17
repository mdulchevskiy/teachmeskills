# Дан файл, содержащий различные даты. Каждая дата - это
# число, месяц и год. Найти самую раннюю дату.
# [02-8.1-ML-29]


def main():
    with open('task_10_03.txt', 'r') as file:
        book = file.readlines()

    dates = [date.rstrip() for date in book]
    dates = [date.split(sep='.') for date in dates]
    dates = list(map(lambda elem: list(map(int, elem)), dates))
    print(dates)

    min_date = dates[0]
    for date in dates:
        if date[2] < min_date[2]:
            min_date = date
        elif date[2] == min_date[2]:
            if date[1] < min_date[1]:
                min_date = date
            elif date[1] == min_date[1]:
                if date[0] <= min_date[0]:
                    min_date = date
    print(min_date)


if __name__ == '__main__':
    main()
