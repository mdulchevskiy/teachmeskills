from django.db import models


class AnimalImage(models.Model):
    url = models.CharField(max_length=255, default=None)
    species = models.CharField(max_length=20, default=None)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=6, default=None)
