# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Переопределить магические методы сравнения(равно, не равно),
# сложения, вычитания, вывод на экран.  Перегрузить конструктор на
# обработку входных параметров вида: одна строка, три числа, другой
# объект класса MyTime, и отсутствие входных параметров.
# [my-oop-02]
# Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/


class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
            total_seconds = self.time_to_seconds()
            self.hours, self.minutes, self.seconds = self.seconds_to_time(total_seconds)
        elif len(args) == 1 and isinstance(args[0], str):
            separator = None
            string = list(args[0])
            for i in range(2):
                if not string[i].isdigit():
                    separator = string[i]
            my_list = args[0].split(sep=separator)
            self.hours, self.minutes, self.seconds = my_list
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours, self.minutes, self.seconds = args[0].hours, args[0].minutes, args[0].seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def time_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, seconds):
        hours = seconds // 3600
        minutes = seconds // 60 % 60
        seconds = seconds % 60
        return hours, minutes, seconds

    def __eq__(self, other):
        return all([self.hours == other.hours,
                    self.minutes == other.minutes,
                    self.seconds == other.seconds])

    def __ne__(self, other):
        return not (self == other)

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

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


def main():
    my_time = MyTime(1, 1, 1)
    my_time2 = MyTime(2, 2, 2)
    print(my_time.hours)
    print(my_time.minutes)
    print(my_time.seconds)
    print(my_time)
    print(my_time != my_time2)
    print(my_time == my_time2)
    print(my_time2 + my_time)
    print(MyTime(3, 4, 5))
    print(MyTime('4-5-6'))
    print(MyTime('4/5/7'))
    print(MyTime('4.5.8'))
    print(MyTime(MyTime(1, 2, 3)))
    print(MyTime(3))


if __name__ == '__main__':
    main()
