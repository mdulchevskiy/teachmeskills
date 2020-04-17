from django.db import models


# 20.06. Описать модель Customer. Поля: имя, фамилия, возраст, профессия.
# python manage.py makemigrations work_20
# python manage.py migrate work_20
class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
