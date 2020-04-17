from django.db import models
from django.db.models import SET_NULL


# 22.01. Создать таблицу Учебной группы(Group).
# Группа характеризуется названием (name). Зарегистрировать модель в админке.
class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Group: {self.name}'


# 22.02. Создать таблицу Студент(Student).
# Студент характеризуется именем (firstname) и фамилией (lastname) и группой к которой он приурочен.
# Зарегистрировать модель в админке.
class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    group = models.ForeignKey('Group', null=True, on_delete=SET_NULL, related_name='students')

    def __str__(self):
        return f'Student: {self.firstname} {self.lastname}'


# 22.03. Создать таблицу Школьный дневник(Diary).
# Дневник характеризуется средним баллом и студентом к которому он приурочен.
# Зарегистрировать модель в админке.
class Diary(models.Model):
    av_mark = models.FloatField()
    student = models.OneToOneField('Student', null=True, on_delete=SET_NULL, related_name='diary')

    def __str__(self):
        return f'Diary: {self.student}'


# 22.04. Создать таблицу Книга(Book).
# Книга характеризуется названием, количеством страниц и студентами у которых эта книга.
# Зарегистрировать модель в админке.
class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    students = models.ManyToManyField('Student', related_name='books')

    def __str__(self):
        return f'Book: {self.title}'
