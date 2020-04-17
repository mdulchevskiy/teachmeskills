# Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на
# таблицу Brand)). Реализовать CRUD(создание, чтение, обновление по id,
# удаление по id) для бренда и машины. Создать пользовательский интерфейс.


from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///task_16_db', echo=False)
Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    brand_name = Column(String)

    def __repr__(self):
        return f'Brand: {self.id} {self.brand_name}'


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)

    brand = relationship('Brand', lazy='subquery', foreign_keys='Car.brand_id', backref='brand')

    def __repr__(self):
        return f'Car: {self.id} {self.model} {self.brand.brand_name}'
