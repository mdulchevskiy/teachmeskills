from django.db import models


class TodoList(models.Model):
    activity = models.CharField(max_length=255, default=None)
    priority = models.IntegerField()
    status = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
