# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from task_15_ui_funcs import choosing_param, choosing_id


engine = create_engine("sqlite:///task_15_db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    amount = Column(Integer)
    comment = Column(String)


def create_table():
    Base.metadata.create_all(engine)


def enter_product():
    title = input('название: ')
    price = float(input('цена: '))
    amount = int(input('количество: '))
    comment = input('комменатарий: ')
    return title, price, amount, comment


def add_product():
    session = Session()
    name, price, amount, comment = enter_product()
    product = Product(
        title=name,
        price=price,
        amount=amount,
        comment=comment,
    )
    session.add(product)
    session.commit()


def get_products():
    session = Session()
    products = session.query(Product).all()
    session.close()
    return products


def get_product(product_id):
    session = Session()
    product = session.query(Product).filter_by(id=product_id).first()
    session.close()
    return product


def print_table():
    products = get_products()
    print('\n************************************')
    print('ID', 'Название'.ljust(10), 'Цена', 'Количество', 'Комментарий', sep='|')
    print('----------------------------------------')
    for product in products:
        print(str(product.id).ljust(2),
              product.title.center(10),
              str(product.price).center(4),
              str(product.amount).center(10),
              str(product.comment).center(11),
              sep='|')
    print('************************************')


def product_update():
    products = get_products()
    chosen_id = choosing_id(products)
    parameter = choosing_param()
    product = get_product(chosen_id)
    new_value = input('\nEnter new value: ')
    setattr(product, parameter, new_value)
    session = Session()
    session.add(product)
    session.commit()
    print(f'Product ID:{chosen_id} successfully updated!')


def product_delete():
    session = Session()
    products = get_products()
    print('\nDeleting product by ID.')
    chosen_id = choosing_id(products)
    product = get_product(chosen_id)
    session.delete(product)
    session.commit()
    print(f'Product ID:{chosen_id} successfully deleted!')
