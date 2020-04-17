# Написать калькулятор с использованием класса Math. Класс принимает
# в качестве аргументов два числа. Определить 4 метода (сложение, вычитание, умножение, деление).
# Реализовать пользовательский интерфейс с бесконечным циклом. Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов (main.py, classes.py, ui_func.py exceptions.py).


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def addition(self):
        return self.a + self.b

    @property
    def subtraction(self):
        return self.a - self.b

    @property
    def multiplication(self):
        return self.a * self.b

    @property
    def division(self):
        return self.a / self.b
