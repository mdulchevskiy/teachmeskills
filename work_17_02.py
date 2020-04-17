# pip install sqlalchemy


from sqlalchemy import create_engine, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker


engine = create_engine('sqlite:///work_17_02_db', echo=False)
Base = declarative_base()

association_table = Table('book_student_association', Base.metadata,
                          Column('student_id', Integer, ForeignKey('student.id')),
                          Column('book_id', Integer, ForeignKey('book.id')),
                          )


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'id: {self.id} Group: {self.name}'


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)

    group = relationship('Group', foreign_keys='Student.group_id', backref='students')

    def __repr__(self):
        return f'id: {self.id} Student: {self.firstname} {self.lastname}'


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    av_mark = Column(Float)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)

    student = relationship('Student', foreign_keys='Diary.student_id', backref=backref('diary', uselist=False))

    def __repr__(self):
        return f'id: {self.id} Diary: {self.student.firstname} {self.student.lastname}'

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages = Column(Integer)

    students = relationship('Student', secondary=association_table, backref='books')

    def __repr__(self):
        return f'id: {self.id} Book: {self.name}'


def main():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    groups_students = session.query(Group, Student).join(Student).filter(Student.firstname == 'Maxim').all()
    print(groups_students)

    book_abc = session.query(Book).filter_by(name='ABC').all()
    if not book_abc:
        book = Book(name='ABC', pages=242)
        updated_students = []
        for group, student in groups_students:
            student.books.append(book)
            updated_students.append(student)
        print(updated_students)
        session.add_all(updated_students)
        session.commit()


if __name__ == '__main__':
    main()
