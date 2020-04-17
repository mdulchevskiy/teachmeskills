import csv


def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        return fields, rows


def write_csv(filename, fields, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def add_to_csv(filename, new_rows, position=None):
    fields, rows = read_csv(filename)
    length = len(fields)
    new_length = len(new_rows)
    if length == new_length:
        if position is None:
            rows.append(new_rows)
        else:
            rows.insert(position, new_rows)
        write_csv(filename, fields, rows)
    else:
        print('Incorrect size of input row')


def del_line_from_csv(filename, position=None):
    fields, rows = read_csv(filename)
    length = len(rows)
    if rows and position is None:
        del rows[-1]
        write_csv(filename, fields, rows)
    elif rows and position <= length:
        del rows[position - 1]
        write_csv(filename, fields, rows)
    else:
        print('Something go wrong. Cant delete')


def product_sum(rows):
    summ = 0
    for row in rows:
        summ += float(row[1]) * float(row[2])
    return summ


def find_expensive(rows):
    max = float(rows[0][1])
    name = rows[0][0]
    for row in rows:
        if float(row[1]) > max:
            max = float(row[1])
            name = row[0]
    return max, name


def find_cheap(rows):
    min = float(rows[0][1])
    name = rows[0][0]
    for row in rows:
        if float(row[1]) < min:
            min = float(row[1])
            name = row[0]
    return min, name


def del_lines_from_csv(filename, n=1):
    fields, rows = read_csv(filename)
    length = len(rows)
    for i in range(n):
        if rows and n <= length:
            rows.pop(-1)
        else:
            print('Something go wrong')
            break
    write_csv(filename, fields, rows)
