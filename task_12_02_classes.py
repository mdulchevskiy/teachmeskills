from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    def dist(self, point1, point2):
        dist = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5
        return dist

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        area = 0.5 * abs((self.a.x - self.c.x) * (self.b.y - self.c.y) - (self.b.x - self.c.x) * (self.a.y - self.c.y))
        return area

    @property
    def perimeter(self):
        dist1 = self.dist(self.a, self.b)
        dist2 = self.dist(self.b, self.c)
        dist3 = self.dist(self.a, self.c)
        return dist1 + dist2 + dist3


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        dist = self.dist(self.a, self.b)
        area = dist ** 2 / 2
        return area

    @property
    def perimeter(self):
        dist = self.dist(self.a, self.b)
        perimeter = (dist / 2 ** 0.5) * 4
        return perimeter
