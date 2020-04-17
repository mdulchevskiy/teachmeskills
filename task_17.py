# pip install sqlalchemy
# python -m unittest task_17.py
# Покрыть тестами функционал.

from unittest import TestCase


class WrongInputError(Exception):
    def __init__(self, message='Wrong input'):
        super().__init__(message)


def validate_args(x, y):
    message = ''
    if not isinstance(x, (int, float)):
        message += f'The first argument type should be int or float. Now it is {type(x)}.\n'
    if not isinstance(y, (int, float)):
        message += f'The second argument type should be int or float. Now it is {type(y)}.\n'
    if message:
        raise WrongInputError(message)


class Math:
    def __init__(self, x, y):
        validate_args(x, y)
        self.x = x
        self.y = y

    def calc_mult(self):
        return self.x * self.y

    def calc_div(self):
        return self.x / self.y


class TestValidateArgs(TestCase):
    def test_first_arg_wrong_type(self):
        x, y = (None, 5)
        with self.assertRaises(WrongInputError) as ex:
            validate_args(x, y)
        exception = ex.exception
        self.assertEqual(
            exception.args[0],
            "The first argument type should be int or float. Now it is <class 'NoneType'>.\n",
        )

    def test_second_arg_wrong_type(self):
        x, y = (2.4, 'string')
        with self.assertRaises(WrongInputError) as ex:
            validate_args(x, y)
        exception = ex.exception
        self.assertEqual(
            exception.args[0],
            "The second argument type should be int or float. Now it is <class 'str'>.\n",
        )

    def test_both_args_wrong_type(self):
        x, y = (Math, validate_args)
        with self.assertRaises(WrongInputError) as ex:
            validate_args(x, y)
        exception = ex.exception
        self.assertEqual(
            exception.args[0],
            "The first argument type should be int or float. Now it is <class 'type'>.\n"
            "The second argument type should be int or float. Now it is <class 'function'>.\n"
        )

    def test_both_args_right_type(self):
        x, y = (10, 2.5)
        self.assertIsNone(validate_args(x, y))


class TestClassMath(TestCase):
    def test_class_create(self):
        math = Math(10, 2.5)
        self.assertEqual(math.x, 10)
        self.assertEqual(math.y, 2.5)

    def test_math_calc(self):
        math = Math(10, 2.5)
        self.assertEqual(math.calc_mult(), 25)
        self.assertEqual(math.calc_div(), 4.0)

    def test_math_exception(self):
        math = Math(10, 0)
        with self.assertRaises(ZeroDivisionError):
            math.calc_div()
