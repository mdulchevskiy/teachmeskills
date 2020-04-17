# Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure.
# Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
# длина радиуса; методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
# Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании.
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
# [my-oop-03]
# Примечание: в рамках задание создать два файла: classes.py и main.py.
# В первом будут описаны все классы, во втором классы будут импортированы и использованы.


from task_12_02_classes import Point, Triangle, Square, Circle


def main():
    point_a = Point(1, 2)
    point_b = Point(1, 1)
    point_c = Point(4, 4)
    radius = 3

    triangle = Triangle(point_a, point_b, point_c)
    square = Square(point_b, point_c)
    circle = Circle(point_a, radius)

    figures = [triangle, square, circle]
    for figure in figures:
        print(f'The area of {figure.__class__.__name__} is {round(figure.area,1)}')


if __name__ == '__main__':
    main()
