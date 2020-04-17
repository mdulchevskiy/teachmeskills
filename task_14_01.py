# Написать программу таймер. Программа при запуске принимает
# имя, фамилию, часы, минуты и секунды. После программа начинает
# обратный отсчет выводя оставшееся время. Программа должна хранить
# файл логирования с информацией о том кто запускал программу и когда.
# Пример:
# 00:00:03
# 00:00:02
# 00:00:01
# ALARM!!!

# python3 task_14_01.py -fn Maxim -ln Dulchevskiy -hs 0 -ms 0 -ss 15


from datetime import datetime
from time import sleep, gmtime, strftime
import argparse


def time_generator(seconds):
    for i in range(seconds):
        seconds -= 1
        yield seconds + 1
        sleep(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-hs', '--hours', required=True, type=int)
    parser.add_argument('-ms', '--minutes', required=True, type=int)
    parser.add_argument('-ss', '--seconds', required=True, type=int)
    args = parser.parse_args()

    with open('task_14_01.txt', 'a') as file:
        file.write(f'{args.first_name}, {args.last_name}, {datetime.now()}.\n')

    seconds = args.hours * 3600 + args.minutes * 60 + args.seconds
    generator = time_generator(seconds)
    for time in generator:
        print(strftime('%H:%M:%S', gmtime(time)))
    print('ALARM!!!')


if __name__ == '__main__':
    main()
