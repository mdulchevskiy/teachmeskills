# pip install sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///work_15_db", echo=True)
metadata = MetaData()
Base = declarative_base()


class Person(Base):
   __tablename__ = 'user_orm_2'
   id = Column(Integer, primary_key=True)
   firstname = Column(String)
   lastname = Column(String)

   def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname


Base.metadata.create_all(engine)
