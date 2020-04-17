# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран. Перегрузить
# конструктор на обработку входных параметров вида: одна строка, три числа,
# другой объект класса MyTime, и отсутствие входных параметров.
# Реализовать нормальное отображение времени (12:65:83 - 13:06:23).


class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
            total_seconds = self.time_to_seconds()
            self.hours, self.minutes, self.seconds = self.seconds_to_time(total_seconds)
        elif len(args) == 1 and isinstance(args[0], str):
            separator = None
            string = list(args[0])
            for i in range(3):
                if not string[i].isdigit():
                    separator = string[i]
            my_list = args[0].split(sep=separator)
            self.hours, self.minutes, self.seconds = list(map(int, my_list))
            total_seconds = self.time_to_seconds()
            self.hours, self.minutes, self.seconds = self.seconds_to_time(total_seconds)
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours, self.minutes, self.seconds = args[0].hours, args[0].minutes, args[0].seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def time_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, seconds):
        hours = seconds // 3600
        hours %= 24
        minutes = seconds // 60 % 60
        seconds = seconds % 60
        return hours, minutes, seconds

    def __str__(self):
        seconds = str(self.seconds).zfill(2)
        minutes = str(self.minutes).zfill(2)
        hours = str(self.hours).zfill(2)
        return f'{hours}:{minutes}:{seconds}'

    def __eq__(self, other):
        return all([self.hours == other.hours,
                    self.minutes == other.minutes,
                    self.seconds == other.seconds])

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.time_to_seconds() < other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __le__(self, other):
        return self.time_to_seconds() <= other.time_to_seconds()

    def __ge__(self, other):
        return self.time_to_seconds() >= other.time_to_seconds()

    def __add__(self, other):
        total_seconds = self.time_to_seconds() + other.time_to_seconds()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        total_seconds = self.time_to_seconds() - other.time_to_seconds()
        if total_seconds < 0:
            return MyTime()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __mul__(self, number):
        total_seconds = self.time_to_seconds() * number
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)


def main():
    my_time1 = MyTime(13, 76, 125)
    my_time2 = MyTime('25-34-76')
    my_time3 = MyTime('8.34.456')
    my_time4 = MyTime('13;76;125')
    my_time5 = MyTime(4)

    print(f'1. MyTime(13,76,125) = {my_time1}')
    print(f'2. MyTime("25-34-76") = {my_time2}')
    print(f'3. MyTime("8.34.456") = {my_time3}')
    print(f'4. MyTime("13;76;125") = {my_time4}')
    print(f'5. MyTime(4) = {my_time5}')
    print('\nMagic methods:\n')
    print(f'{my_time1} == {my_time2} is {my_time1 == my_time2}')
    print(f'{my_time1} != {my_time3} is {my_time1 != my_time3}')
    print(f'{my_time1}  > {my_time3} is {my_time1 > my_time3}')
    print(f'{my_time1} >= {my_time3} is {my_time1 >= my_time3}')
    print(f'{my_time1}  < {my_time3} is {my_time1 < my_time3}')
    print(f'{my_time1} <= {my_time3} is {my_time1 <= my_time3}')
    print(f'{my_time1} <= {my_time4} is {my_time1 <= my_time4}')
    print(f'{my_time1} >= {my_time4} is {my_time1 >= my_time4}')
    print(f'{my_time1}  + {my_time2} is {my_time1 + my_time2}')
    print(f'{my_time5}  - {my_time3} is {my_time5 - my_time3}')
    print(f'{my_time3}  * 2        is {my_time3 * 2}')


if __name__ == '__main__':
    main()
