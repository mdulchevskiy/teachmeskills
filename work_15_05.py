# pip install sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper


class User:
   def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname


engine = create_engine("sqlite:///work_15_db", echo=True)

metadata = MetaData()
users_table = Table(
    'user_orm_1', metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String), )
metadata.create_all(engine)
mapper(User, users_table)

user = User('Alex', 'Varkalov')
