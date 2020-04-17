# pip install django


# 22.02. Создать две группы(одну через интерпретатор, другую через админку).
# Добавить в каждую по три студента.
# Все команды выполняются в шеле (python manage.py shell).
def work_22_02():
    from work_22.models import *
    group1 = Group.objects.create(name='14DKK')
    group2 = Group.objects.create(name='18DUI')
    Student.objects.create(firstname='Maxim', lastname='Dulchevskiy', age=23, group=group1)
    Student.objects.create(firstname='Alex', lastname='Malyavko', age=23, group=group1)
    Student.objects.create(firstname='Nick', lastname='Mihalevich', age=23, group=group1)
    Student.objects.create(firstname='Vlad', lastname='Sudilovskiy', age=22, group=group2)
    Student.objects.create(firstname='Nastya', lastname='Ustsimenko', age=23, group=group2)
    Student.objects.create(firstname='Alex', lastname='Varkalov', age=25, group=group2)


# 22.03. Получить всех студентов и создать для каждого дневник (в интерпретаторе).
# Создать студента и его дневник через админку.
# Все команды выполняются в шеле (python manage.py shell).
def work_22_03():
    groups = Group.objects.filter().all()
    students = []
    av_marks = [4, 5, 6, 7, 8, 9, 10]
    for group in groups:
        students.extend(group.students.all())
    for i, student in enumerate(students):
        Diary.objects.create(av_mark=av_marks[i], student=student)


# 22.04. Создать 5 книг. Получить всех студентов и добавить каждому студенту эти пять книг(в интерпретаторе).
# Добавить книгу через админку и добавить трем студентам эту книгу.
def work_22_04():
    for j in range(1, 6):
        Book.objects.create(title=f'Book {j}', pages=j * 10)
    books = Book.objects.filter().all()
    for book in books:
        book.students.add(*students)
