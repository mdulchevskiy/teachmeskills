# pip install sqlalchemy
# python -m unittest work_17_03.py


from unittest import TestCase


def div(a, b):
    return a / b


class DivTestCase(TestCase):
    def test_normal(self):
        result = div(4, 2)
        self.assertEqual(result, 2)

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)
