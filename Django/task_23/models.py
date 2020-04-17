from django.db import models


class Fio(models.Model):
    name = models.CharField(max_length=255, default=None)
    surname = models.CharField(max_length=255, default=None)


# python manage.py shell
# from task_23.models import Fio
# Fio.objects.create(name='Maxim', surname='Dulchevskiy')
# Fio.objects.create(name='Nastya', surname='Ustsimenko')
