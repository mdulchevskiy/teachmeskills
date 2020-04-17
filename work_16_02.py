# pip instal sqlalchemy


from sqlalchemy import create_engine, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker


engine = create_engine('sqlite:///work_16_02_db', echo=True)
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

    students = session.query(Student).filter().all()
    diaries = session.query(Diary).filter().all()
    books = session.query(Book).filter().all()

    if not students:
        group1 = Group(name='14DKK')
        group2 = Group(name='18DUI')
        student1 = Student(firstname='Alex', lastname='Malyavko', group=group1)
        student2 = Student(firstname='Nick', lastname='Mihalevich', group=group1)
        student3 = Student(firstname='Maxim', lastname='Dulchevskiy', group=group2)
        student4 = Student(firstname='Nastya', lastname='Ustsimenko', group=group2)

        session.add_all([
            group1, group2,
            student1, student2, student3, student4,
        ])
        session.commit()
    elif not diaries:
        av_mark_dict = {
            'Malyavko': 5.4,
            'Mihalevich': 6.4,
            'Dulchevskiy': 8.8,
            'Ustsimenko': 9.7,
        }
        for student in students:
            diary = Diary(av_mark=av_mark_dict[student.lastname], student=student)
            session.add(diary)
            session.commit()
    elif not books:
        book1 = Book(name='Book 1', pages=10, students=students)
        book2 = Book(name='Book 2', pages=20, students=students)
        book3 = Book(name='Book 3', pages=30, students=students)
        book4 = Book(name='Book 4', pages=40, students=students)
        book5 = Book(name='Book 5', pages=50, students=students)

        session.add_all([
            book1, book2, book3, book4, book5,
        ])
        session.commit()


if __name__ == '__main__':
    main()
