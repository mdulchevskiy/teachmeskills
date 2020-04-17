# Создать скрипт, который принимает
# имя фамилию и возраст и дописывает их в csv файл
# Terminal: python3 work_14_04.py -fn Maxim -ln Dulchevskiy --age 22


import argparse
import csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-ag', '--age', required=True)
    args = parser.parse_args()
    try:
        with open('work_14_04.txt') as file:
            pass
    except:
        with open('work_14_04.txt', 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['First name','Last name','Age'])
    finally:
        with open('work_14_04.txt', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([args.first_name, args.last_name, args.age])


if __name__ == '__main__':
    main()
