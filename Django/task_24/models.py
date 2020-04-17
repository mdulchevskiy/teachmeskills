from django.db import models


class NatureImage(models.Model):
    link = models.CharField(max_length=255, default=None)
    width = models.IntegerField()
    height = models.IntegerField()
    comment = models.CharField(max_length=255, default=None)
