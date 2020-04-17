# pip install sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///work_15_db", echo=True)

metadata = MetaData()
Base = declarative_base()


class Person(Base):
    __tablename__ = 'user_orm'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Base.metadata.create_all(engine)

# добавление записи в бд
Session = sessionmaker(bind=engine)

session = Session()
session.add(Person('Alex', 'Varkalov'))
session.add_all([Person('Alex', 'Petrov'), Person('Ann', 'Ivanova')])
session.commit()

# создание запроса Query
person = session.query(Person).filter_by(firstname="Alex").first()
person1 = session.query(Person).filter(Person.firstname == "Alex").first()
person2 = session.query(Person).filter(
    and_(Person.firstname == "Alex",
         Person.lastname == "Varkalov",)
).all()
print(type(person1))
print(type(person2))
for elem in person2:
    print(type(person2), person2)
