# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных.
# Создать иерархию ошибок.


class Book:
    def __init__(self, pages_amount, year, author, price):
        self.pages_amount = pages_amount
        self.year = year
        self.author = author
        self.price = price

        if not isinstance(pages_amount, int):
            if isinstance(pages_amount, str):
                raise PagesStrError
            elif isinstance(pages_amount, float):
                raise PagesFloatError
            else:
                raise PagesAmountError

        if not isinstance(year, int):
            if isinstance(year, str):
                raise YearStrError
            elif isinstance(year, float):
                raise YearFloatError
        elif year < 0 or year > 2019:
            raise YearOutOfRangeError

        if not isinstance(author, str):
            raise AuthorError
        else:
            if not author.isalpha():
                raise AuthorTypeError

        if isinstance(price, str):
            raise PriceStrError
        elif price < 0:
            raise PriceOutOfRangeError


class ClassBookError(Exception):
    def __init__(self, message='Something go wrong.'):
        super().__init__(message)


class PagesAmountError(ClassBookError):
    def __init__(self, message='Incorrect input for number of pages.'):
        super().__init__(message)


class PagesStrError(PagesAmountError):
    def __init__(self, message='Number of pages should be int, not str.'):
        super().__init__(message)


class PagesFloatError(PagesAmountError):
    def __init__(self, message='Number of pages should be int, not float.'):
        super().__init__(message)


class YearError(ClassBookError):
    def __init__(self, message='Incorrect input for year.'):
        super().__init__(message)


class YearStrError(YearError):
    def __init__(self, message='Year should be int, not str.'):
        super().__init__(message)


class YearFloatError(YearError):
    def __init__(self, message='Year should be int, not float.'):
        super().__init__(message)


class YearOutOfRangeError(YearError):
    def __init__(self, message='Year is out of range.'):
        super().__init__(message)


class AuthorError(ClassBookError):
    def __init__(self, message='Incorrect input for author.'):
        super().__init__(message)


class AuthorTypeError(AuthorError):
    def __init__(self, message='Year should be str.'):
        super().__init__(message)


class PriceError(ClassBookError):
    def __init__(self, message='Incorrect input for price.'):
        super().__init__(message)


class PriceStrError(PriceError):
    def __init__(self, message='Price should be int or float, not str.'):
        super().__init__(message)


class PriceOutOfRangeError(PriceError):
    def __init__(self, message='Price is out of range.'):
        super().__init__(message)


def main():
    book = Book(323, 2018, 'maxim', 23)


if __name__ == '__main__':
    main()
