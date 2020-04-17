from django.db import models


class Users(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
    profession = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'User: {self.pk}-{self.name}'
