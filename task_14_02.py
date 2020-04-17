# Создать программу Pomodoro.
# https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BF%D0%BE%D0%BC%D0%B8%D0%B4%D0%BE%D1%80%D0%B0
# На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут),
# длину перерыва(по-умолчанию 5 минут), количество циклов(по-умолчанию 4) и название задачи.
# Программа указывает оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
# после сигнализирует о начале нового цикла фокусировки. Программа должна вести файл лога о всех запусках.

# python3 task_14_02.py -fn Maxim -ln Dulchevskiy -ft 7 -bt 3 -am 2 -tn Test


import argparse
import os
from time import sleep, gmtime, strftime
from datetime import datetime


def wait_time(total_seconds):
    total_seconds = total_seconds / 60
    while total_seconds:
        print(strftime('%H:%M:%S', gmtime(total_seconds)))
        total_seconds -= 1
        sleep(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-ft', '--focus-time', default=25, type=int)
    parser.add_argument('-bt', '--break-time', default=5, type=int)
    parser.add_argument('-am', '--amount', default=4, type=int)
    parser.add_argument('-tn', '--task-name', required=True)
    args = parser.parse_args()

    amount = args.amount
    focus_time = args.focus_time * 60
    break_time = args.break_time * 60
    is_break = False
    print(args.task_name)
    while amount > 0:
        if not is_break:
            print('FOCUS!')
            wait_time(focus_time)
            is_break = True
            amount -= 1
        else:
            print('BREAK!')
            wait_time(break_time)
            is_break = False

    file_path = os.path.realpath(__file__)
    dir_name = os.path.dirname(file_path)
    with open(f'{dir_name}/task_14_02.txt', 'a') as f:
        f.write(f'{args.first_name}, {args.last_name}, {datetime.now()}.\n')


if __name__ == '__main__':
    main()
