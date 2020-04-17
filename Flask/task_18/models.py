# Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
# Модель продукта состоит из id, name, price, amount, comment.
# На главной странице отображена краткая информация (id, name, price, amount) по всем продуктам.
# При нажатии на продукт происходит перенаправление на детализированную информацию по продукту.
# На детализированной странице продукта есть кнопки позволяющие отредактировать и удалить продукт.


from settings import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    comment = db.Column(db.String(200))

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return f'Product: {self.id}-{self.name}'
