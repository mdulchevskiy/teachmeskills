# Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.


class Car:
    def __init__(self, make, model, year, speed=0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def get_make(self):
        return self.__make

    @property
    def get_model(self):
        return self.__model

    @property
    def get_year(self):
        return self.__year

    @property
    def get_speed(self):
        return self.__speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        if self.__speed:
            self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def speed_printing(self):
        print(f'Speed: {self.__speed}')

    def turning(self):
        self.__speed = -self.__speed


def car_info_printing(car):
    print(f'\nMake: {car.get_make}\nModel: {car.get_model}\nYear: {car.get_year}\nSpeed: {car.get_speed} km/h\n')


def main():
    car = Car('Ford', 'Mustang', '2005')
    car_info_printing(car)

    car.decrease_speed()
    car.speed_printing()

    car.increase_speed()
    car.increase_speed()
    car.speed_printing()

    car.stop()
    car_info_printing(car)

    car.increase_speed()
    car.turning()
    car_info_printing(car)


if __name__ == '__main__':
    main()
