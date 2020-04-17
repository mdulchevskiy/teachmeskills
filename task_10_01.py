# Создать csv файл с данными следующей структуры: Имя, Фамилия, Восраст.
# Создать отчетный файл с информацией по количеству людей входящих в ту
# или иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.


from csv_utils import (write_csv, read_csv)
from itertools import repeat
from math import inf
import json


def main():
    filename = 'task_10_01.txt'
    fields = ['Имя', 'Фамилия', 'Возраст']
    rows = [
        ['Максим', 'Дульчевский', 22],
        ['Влад', 'Судиловский', 21],
        ['Никита', 'Михалевич', 27],
        ['Вадим', 'Тарасевич', 18],
    ]
    groups = [(1, 12), (13, 18), (19, 25), (26, 40), (41, inf)]

    write_csv(filename, fields, rows)

    new_fields, new_rows = read_csv(filename)
    print(new_fields)
    for line in new_rows:
        print(line)

    in_groups = list(repeat(0, len(groups)))
    for ind, group in enumerate(groups):
        for row in rows:
            if group[0] <= row[2] <= group[1]:
                count = in_groups[ind]
                count += 1
                in_groups[ind] = count

    group_report = {f'Group {group[0]}-{group[1]}': in_groups[ind] for ind, group in enumerate(groups)}

    with open('task_10_01_report.json', 'w') as file:
        data = json.dumps(group_report)
        file.write(data)

    with open('task_10_01_report.json') as file:
        data = json.loads(file.read())
        for key, value in data.items():
            print(key, value)


if __name__ == '__main__':
    main()
