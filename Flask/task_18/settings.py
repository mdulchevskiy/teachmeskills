# Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
# Модель продукта состоит из id, name, price, amount, comment.
# На главной странице отображена краткая информация (id, name, price, amount) по всем продуктам.
# При нажатии на продукт происходит перенаправление на детализированную информацию по продукту.
# На детализированной странице продукта есть кнопки позволяющие отредактировать и удалить продукт.


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_18_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'
db = SQLAlchemy(app)
