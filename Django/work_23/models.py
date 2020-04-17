from django.db import models


# 23.01. Создать модель продукта. Модель описывается названием, ценой, количеством и комментарием.
# Создать 5 записей в базе данных.
class Product(models.Model):
    name = models.CharField(max_length=255, default=None)
    price = models.FloatField()
    amount = models.IntegerField()
    comment = models.CharField(max_length=255)


# python manage.py shell
# from work_23.models import Product
# Product.objects.create(name='Banana', price=2.3, amount=2, comment='Yellow')
# Product.objects.create(name='Apple', price=3.3, amount=2, comment='Green')
# Product.objects.create(name='Chocolate', price=2, amount=1, comment='Alpen Gold')
# Product.objects.create(name='Coke', price=2.7, amount=1, comment='Cola')
# Product.objects.create(name='Chips', price=2.9, amount=3, comment='Lays')
